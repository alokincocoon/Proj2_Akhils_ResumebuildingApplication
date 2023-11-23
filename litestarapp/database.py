from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Declaring engine for DB
engine = create_engine("postgresql://postgres:postgres@127.0.0.1:5432/resume_builder")
# Function to create a session factory with which to create individual database instances.
Session = sessionmaker(bind=engine)
# Creating session instance
session = Session()