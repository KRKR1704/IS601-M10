# Author: Roopesh Kumar Reddy Kaipa
# Date: 11/10/2025
import pytest
from sqlalchemy import text

import app.database as app_database
from app import database_init


def test_get_db_and_init_drop():
    """Exercise get_db generator and init_db/drop_db functions to ensure
    these runtime helpers are covered by tests.
    """
    # Ensure init/create works without raising
    database_init.init_db()

    # Use the get_db generator to obtain a session
    gen = app_database.get_db()
    db = next(gen)

    # Run a small query
    result = db.execute(text("SELECT 1")).scalar()
    assert result == 1

    # Close the generator to trigger cleanup
    gen.close()

    # Finally, drop the tables to clean up
    database_init.drop_db()


def test_call_database_main(db_session):
    """Call database_init.main() after test fixtures prepared to exercise the main guard path.

    The `db_session` fixture ensures the test DB engine is patched before calling main().
    """
    import app.database_init as database_init

    # Should not raise (uses patched engine from conftest)
    database_init.main()


def test_run_module_guard_with_patched_engine():
    """Run app.database_init as a __main__ module while ensuring the imported
    `app.database.engine` is a safe in-memory engine to avoid real Postgres connections.
    """
    import sys
    import types
    import runpy
    from sqlalchemy import create_engine

    # create a temporary in-memory engine and patch sys.modules
    fake_engine = create_engine("sqlite:///:memory:")
    fake_db_mod = types.ModuleType("app.database")
    fake_db_mod.engine = fake_engine

    original = sys.modules.get("app.database")
    try:
        sys.modules["app.database"] = fake_db_mod
        # Running the module will execute the module guard which calls main()
        import warnings
        with warnings.catch_warnings():
            # Silence the runtime warning emitted by runpy about module in sys.modules
            warnings.filterwarnings(
                "ignore",
                message=r".*found in sys.modules after import of package 'app', but prior to execution of 'app.database_init'.*",
                category=RuntimeWarning,
            )
            runpy.run_module('app.database_init', run_name="__main__")
    finally:
        # restore original module if any
        if original is not None:
            sys.modules["app.database"] = original
        else:
            del sys.modules["app.database"]

