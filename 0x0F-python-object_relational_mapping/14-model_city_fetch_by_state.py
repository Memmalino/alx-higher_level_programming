#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(db_username, db_password, db_name),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    from_session = session()

    result = (from_session.query(State, City)
              .filter(State.id == City.state_id)
              .order_by(City.id).all())

    for state, city in result:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    from_session.close()
