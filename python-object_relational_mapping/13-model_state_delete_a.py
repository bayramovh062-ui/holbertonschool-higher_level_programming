#!/usr/bin/python3
"""
this code removes all rows which
one it contains a letter
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
                    )
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_rows = (
                session.query(State)
                .filter(State.name.op(('LIKE BINARY')('%a%')))
                .all()
            )
    for delete_row in delete_rows:
        session.delete(delete_row)
    session.commit()
    session.close()
