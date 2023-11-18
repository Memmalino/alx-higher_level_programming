#!/usr/bin/python3
"""Script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check for correct number of command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Database connection setup
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database), pool_pre_ping=True)

    # Bind the engine to the Base class
    Base.metadata.create_all(bind=engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State with a City
    new_state = State(name="California", cities=[City(name="San Francisco")])

    # Add and commit the new State to the database
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()

