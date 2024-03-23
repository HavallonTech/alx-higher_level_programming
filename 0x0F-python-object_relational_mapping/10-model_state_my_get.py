#!/usr/bin/python3
"""
    prints the State object with the name passed as argument from the
    database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # connect to db using create_engine() and interact with db using
    # +sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    instance_session = Session()

    # Query and filter states
    state = instance_session.query(State).filter(State.name == argv[4]).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
        session.close()
