#!/usr/bin/python3
"""update the state name with the id '2' to New Mexico"""

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
    state = session.query(State).filter_by(id=2).first()
    state.name = 'New Mexico'
    session.commit()
