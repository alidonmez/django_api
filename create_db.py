from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists,create_database

def validate_database():
     engine = create_engine('postgresql://docker:docker@localhost/form')
     if not database_exists(engine.url): 
         create_database(engine.url)     
         print(f"New Database Created{str(database_exists(engine.url))}")
     else:
         print("Database Already Exists")

validate_database()