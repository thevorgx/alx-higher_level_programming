#!/usr/bin/python3
"""add 'Louisiana' to the table 'State' and print that state id"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                         argv[2], argv[3])
    engine = create_engine(db_url)

    make_session = sessionmaker(bind=engine)
    session = make_session()
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)
