from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://client:uw0ntgue22@localhost:5432/flight", echo=True)

Base = declarative_base()



print(database_exists(engine.url))