from sqlalchemy import Column, Integer, String, Float
from database import Base, engine

# Define the Item model that represents your database table
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)

# Create the tables in the database
Base.metadata.create_all(bind=engine)