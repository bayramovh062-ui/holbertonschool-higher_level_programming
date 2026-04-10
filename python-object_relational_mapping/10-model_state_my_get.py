#!/usr/bin/python3
"""
this code shows us a row from state table
and this row's state name should be
user's input otherwise print Not found
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4].strip("'")
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'/format(
                        username, password, db_name
                    ),
                pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    state = (
                session.query(State)
                .filter(State.name == state_name)
                .first()
            )
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))
    session.close()
