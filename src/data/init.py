"""This module is responsible for initializing the database with entities
"""

from data.database import Base, engine

from data.models.Product import *

Base.metadata.create_all(bind=engine)