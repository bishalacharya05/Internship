from utils.database_utils import Base
from sqlalchemy import Column, Integer,String, Boolean,ForeignKey
from sqlalchemy.orm import relationship

#todo class inherits the Base class which is the decelarative base created using declarative_base from SQLalchemy
#this helps to establish the connection between model class and the database table
class Todo(Base):
    __tablename__="Todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    completed= Column(Boolean, nullable=False)

    #foreign key to establish relationship with user table
    owner_id = Column(Integer, ForeignKey("users.id"))

    #relationship:many todos -> one user
    user = relationship("User", back_populates="todos")
