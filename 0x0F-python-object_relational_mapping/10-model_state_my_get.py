#!/usr/bin/python3
"""querie to retrieves all states print the state.id matching
the state.name, print nothing ig not found using sqlalchemy"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                         argv[2], argv[3])
    to_find = argv[4]
    engine = create_engine(db_url)

    make_session = sessionmaker(bind=engine)
    session = make_session()

    states = session.query(State).all()
    found = 0
    for state in states:
        if state.name == to_find:
            print("{}".format(state.id))
            found = 1
    if found == 0:
        print("Not found")
