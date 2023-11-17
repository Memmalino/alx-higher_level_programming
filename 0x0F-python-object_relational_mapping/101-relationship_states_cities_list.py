#!/usr/bin/python3
"""Script that lists all State objects and corresponding City objects
   contained in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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
              .join(City)
              .order_by(State.id, City.id).all())

    for state, city in result:
        print('{}: {}'.format(state.name, city))

    from_session.close()
