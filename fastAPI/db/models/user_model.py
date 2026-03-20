from utils.database_utils import Base
from sqlalchemy import Column, Integer,String,Boolean
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    is_admin = Column(Boolean, nullable=False)  # 0 for regular user, 1 for admin

    #relationship:one user -> many todos
    todos = relationship("Todo", back_populates="user", cascade="all, delete")

