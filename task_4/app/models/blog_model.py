from sqlalchemy.orm import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String,DateTime
from datetime import datetime, timezone

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer,primary_key=True, index= True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    author= Column(String, nullable=False)
    created_date = Column(
    DateTime(timezone=True),
    default=lambda: datetime.now(timezone.utc)
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, index= True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
