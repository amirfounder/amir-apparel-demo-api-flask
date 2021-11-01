from sqlalchemy import Column, Integer, String
from data.database import Base

class Product(Base):
  __tablename__ = 'products'
  
  id = Column('id', Integer, primary_key=True)
  name = Column('name', String)
  type = Column('type', String)

