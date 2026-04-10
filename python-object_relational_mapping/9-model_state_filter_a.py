#!/usr/bin/python3
"""
this code shows us state table's row
but only rows which one state_name contains a symbol
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:]
    engine = create_engine(
                    'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            username, password, db_name
                        ),
                    pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    filtered_states = (
                session.query(State)
                .filter(State.name.op('LIKE BINARY')('%a%'))
                .order_by(State.id)
                .all()
            )
    for state in filtered_states:
        print("{}: {}".format(state.id, state.name))
    session.close()
