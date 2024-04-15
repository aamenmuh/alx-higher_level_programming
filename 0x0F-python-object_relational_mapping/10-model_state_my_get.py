#!/usr/bin/python3
"""
List all states using ORM
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).filter(State.name == sys.argv[4]).first()

    if (not state):
        print("Not found")
    else:
        print(state.id)
