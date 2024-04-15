#!/usr/bin/python3
"""
List all states using ORM
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}\
            :{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    state = sessions.query(State).order_by(State.id).first()

    if (not state):
        print("Nothing")
    else:
        print(f"{state.id}: {state.name}")
