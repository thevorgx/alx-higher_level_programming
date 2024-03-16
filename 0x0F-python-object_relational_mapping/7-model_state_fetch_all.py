#!/usr/bin/python3
"""retrieves states name with the id at the beginning,
ordered by the state.id using sqlalchemy"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                         argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    make_session = sessionmaker(bind=engine)
    session = make_session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(state.id, ":", state.name)
