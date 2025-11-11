# Author: Roopesh Kumar Reddy Kaipa
# Date: 11/10/2025
from app.database import engine
from app.models.user import Base


def init_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)


def main():
    """CLI entrypoint: initialize the database.

    This function exists so tests can call it directly (and avoid running
    module-level code via runpy which can be brittle)."""
    init_db()


if __name__ == "__main__":
    main()