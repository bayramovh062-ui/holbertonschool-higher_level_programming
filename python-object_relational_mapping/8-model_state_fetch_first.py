#!/usr/bin/python3
"""
this code shows us the first state object
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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
    states = session.query(State).order_by(State.id).all()
    print("{}: {}".format(states[0].id, states[0].name))
    session.close()
