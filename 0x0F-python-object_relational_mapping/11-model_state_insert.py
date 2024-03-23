#!/usr/bin/python3
"""
    adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # connect to db using create_engine() and interact with db using
    # +sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    instance_session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session and commit to the database
    instance_session.add(new_state)
    instance_session.commit()

    # Print the new state's ID
    print(new_state.id)
    session.close()
