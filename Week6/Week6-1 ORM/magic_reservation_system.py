from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

from cinema_orm import Base, Movie, Projection, Reservation

engine = create_engine("sqlite:///university.db")
# will create all tables
Base.metadata.create_all(engine)

# Session is our Data Mapper
session = Session(bind=engine)

def show_movies(self):
	session = Session(bind=engine)
	session.query