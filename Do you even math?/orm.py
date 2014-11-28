from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import desc
from sqlalchemy.orm import Session
import sys

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    max_score = Column(Integer)

    def __str__(self):
        return "{} --- Record {}".format(self.name, self.max_score)


engine = create_engine("sqlite:///math_players.db")

Base.metadata.create_all(engine, checkfirst=True)    # we activete this only if we want
# to create a new table.

session = Session(bind=engine)


def is_empty(arr):
    return len(arr) == 0


def registration():
    given_name = input("Type your name for a registration here: ")
    session.add(Player(name=given_name, max_score=0))
    curr_player = session.query(Player).filter(Player.name == given_name).all()
    print("Successfully Registered!")
    return curr_player[0]
    #sys.exit()
    #session.commit()


def see_all_registered_players():
    for player in session.query(Player):
        print (player)


def login():
    login_name = input("Type your name: ")
    curr_player = session.query(Player).filter(Player.name == login_name).all()
    if is_empty(curr_player):
        print ("You failed to login. Log in again or register! ")
        option = input("Type <register> or <login> to choose your option.")
        if option == "register":
            curr_player = registration()
            return curr_player
            session.commit()
        elif option == "login":
            curr_player = login()
            return curr_player
        else:
            print ("Invalid command. Try again!")
            curr_player = login()
            return curr_player
    else:
        print("You are logged in as: " + curr_player[0].name)
        return curr_player[0]
    session.commit()
