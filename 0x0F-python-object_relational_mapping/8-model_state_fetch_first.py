#!/usr/bin/python3
"""a script that prints the first State object from the
database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = session.query(State).order_by(State.id).first()
    print("Nothing" if not state_name else "{}: {}".format(
        state_name.id, state_name.name))
