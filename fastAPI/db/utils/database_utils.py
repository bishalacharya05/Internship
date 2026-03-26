#Database connection with ORM SQLAlchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker
from sqlalchemy.orm import declarative_base
import os
from dotenv import load_dotenv
#conneting to postgres database using url and the name of the database todo_db

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
#this is engine function form sqlalchemy and it sonfigures the session to be used for database operation
engine = create_async_engine(DATABASE_URL, echo=True,connect_args={"ssl": None})

#it configure the session to be used for database operations
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession,  # IMPORTANT
    expire_on_commit=False,autoflush=False,autocommit=False)

#it is the base model which serves for creating database tables later
Base = declarative_base()

#this function is used as to get the database session
#it open the database connection and give it to the api function and close automatically after the request is finished
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)