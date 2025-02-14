
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import sqlalchemy as sa
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Load database settings from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todos.db")

# Create engine with dynamic database support
engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# SQLAlchemy model for Todo
class Todo(Base):
    __tablename__ = "todos"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.String, index=True)
    completed = sa.Column(sa.Boolean, default=False)

# Create the database tables if using SQLite (not needed for other DBs)
if "sqlite" in DATABASE_URL:
    Base.metadata.create_all(bind=engine)