#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    _session = session()

    query = _session.query(State.id).filter(State.name == sys.argv[4]).first()
    if query is None:
        print('Not found')
    else:
        print(query[0])
