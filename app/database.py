# Author: Roopesh Kumar Reddy Kaipa
# Date: 11/10/2025
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

from .config import settings

def get_engine(database_url: str = settings.DATABASE_URL):
    """
    Create and return a new SQLAlchemy engine.

    Args:
        database_url (str): The database connection URL.

    Returns:
        Engine: A new SQLAlchemy Engine instance.
    """
    try:
        engine = create_engine(database_url, echo=True)
        return engine
    except SQLAlchemyError as e:
        print(f"Error creating engine: {e}")
        raise

def get_sessionmaker(engine):
    """
    Create and return a new sessionmaker.

    Args:
        engine (Engine): The SQLAlchemy Engine to bind the sessionmaker to.

    Returns:
        sessionmaker: A configured sessionmaker factory.
    """
    return sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
engine = get_engine()
SessionLocal = get_sessionmaker(engine)
Base = declarative_base()

def get_db():
    """
    Dependency function that provides a database session.

    This function can be used with FastAPI's dependency injection system
    to provide a database session to your route handlers.

    Yields:
        Session: A SQLAlchemy Session instance.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
