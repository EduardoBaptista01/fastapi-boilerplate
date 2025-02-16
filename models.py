
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from datetime import datetime
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
    id = sa.Column(sa.Integer, primary_key=True)
    title: Mapped[str]  = mapped_column(sa.String(50), index=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(sa.DateTime, nullable=False, server_default=sa.func.now())
    completed: Mapped[bool] = mapped_column(sa.Boolean, nullable=True, default=False)

# Create the database tables if using SQLite (not needed for other DBs)
if "sqlite" in DATABASE_URL:
    Base.metadata.create_all(bind=engine)