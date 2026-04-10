#!/usr/bin/python3
"""
this codes shows us state table's information
with using sqlalchemy
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, name_db = sys.argv[1:]
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                        username, password, name_db
                    ),
                pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id, state.name).all()
    for state in states:
        print("{}:{}".format(state.id, state.name))
    session.close()
