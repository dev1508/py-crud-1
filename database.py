from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy database URL for SQLite. You can switch to PostgreSQL with 'postgresql://user:password@localhost/dbname'
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal class: Used to create a new database session for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
Base = declarative_base()

# Dependency: Get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()