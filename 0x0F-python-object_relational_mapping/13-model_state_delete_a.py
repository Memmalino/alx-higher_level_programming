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
    from_session = session()

    state = from_session.query(State).filter(State.name.like('%a%')).all()
    for s_state in state:
        from_session.delete(s_state)
    from_session.commit()
