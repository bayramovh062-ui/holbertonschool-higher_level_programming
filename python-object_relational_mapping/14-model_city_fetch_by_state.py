#!/usr/bin/python3
"""
this code shows us state_name city_id and city_name
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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
    city_and_state_information = (
                session.query(State, City)
                .filter(State.id == City.state_id)
                .order_by(City.id)
                .all()
            )
    for STate, CIty in city_and_state_information:
        print("{}: ({}) {}".format(STate.name, CIty.id, CIty.name))
    session.close()
