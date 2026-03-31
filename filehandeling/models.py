from sqlalchemy import Column, Integer, String, LargeBinary
from database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    content_type = Column(String)
    data = Column(LargeBinary)