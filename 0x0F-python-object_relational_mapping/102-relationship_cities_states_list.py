#!/usr/bin/python3
"""
A python script that creates the State "California" with the City
"San Francisco" from the database hbtn_0e_100_usa
"""
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City).order_by(City.id).all()

    for cities in results:
        print(f"{cities.id}: {cities.name} -> {cities.state.name}")
    session.close()
