#!/usr/bin/python3
"""
List all states using ORM
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(f"mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.arg[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = sessions.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
