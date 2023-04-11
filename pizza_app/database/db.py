# creating and connecting the db with our FastApi App
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 



POSTGRES_DATABASE_URL = "postgresql://postgres:admin123@localhost/pizza_delivery"

engine = create_engine(POSTGRES_DATABASE_URL, echo= True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# creates db session object for each request 
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close