from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship

Base = declarative_base()

# Our class will be mapped to a table with name student
# Each field is a Column with the given type and constraints


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)


class Projection(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship(Movie, backref="projections")
    type = Column(String)
    date = Column(String)
    time = Column(String)


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey("projections.id"))
    projection = relationship(Projection, backref = "reservations")
    row = Column(Integer)
    col = Column(Integer)


engine = create_engine("sqlite:///cinema.db")
# will create all tables
Base.metadata.create_all(engine)

session = Session(bind=engine)

session.add_all([
    Movie(name="The Hunger Games: Catching Fire", rating=7.9),
    Movie(name="Wreck it Ralph", rating=7.8),
    Movie(name="Her", rating=8.3)
])

hunger_games = session.query(Movie).filter(Movie.name=="The Hunger Games: Catching Fire").one()
hunger_games.projections = [
    Projection(type="action", date="12.13.2013", time="22:30"),
    Projection(type="action", date="11.13.2013", time="21:30"),
    Projection(type="action", date = "12.22.2013", time = "20:30")]

wreck_it = session.query(Movie).filter(Movie.name== "Wreck it Ralph").one()
wreck_it.projections = [
    Projection(type="thriller", date="12.13.2013", time="22:30"),
    Projection(type="thriller", date="12.04.2013", time="22:30")
]

drago = session.query(Projection).filter(Projection.id==1).one()
drago.reservations = [
    Reservation(username="Misho", row = 2, col = 3),
    Reservation(username="Tisho", row = 3, col = 3),
    Reservation(username="Kisho", row = 4, col = 3)
]

session.commit()
