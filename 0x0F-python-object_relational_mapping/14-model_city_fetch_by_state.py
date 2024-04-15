#!/usr/bin/python3
"""
List all states using ORM
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_cities = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in state_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
