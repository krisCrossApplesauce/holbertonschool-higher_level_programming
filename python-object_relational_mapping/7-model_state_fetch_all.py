#!/usr/bin/python3
"""
Write a script that lists all State objects
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=eng)
    sess = Session()

"""
I DON'T UNDERSTAND THIS!!!
THIS IS THE SORT OF THING I NEED A TEACHER FOR!!!
I WANT TO UNDERSTAND THIS, BUT THERE'S NOT ENOUGH TIME!!!
AND THIS IS THE SORT OF SUBJECT THAT I NEED MORE DIRECT GUIDANCE WITH!!!
THIS IS RIDICULOUSLY FRUSTRATING!!!!!!!!
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!!
"""
