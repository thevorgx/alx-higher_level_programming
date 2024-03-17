#!/usr/bin/python3
"""retrieves states name with the id at the beginning,
ordered by the state.id using sqlalchemy"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State, City


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                         argv[2], argv[3])
    engine = create_engine(db_url)

    make_session = sessionmaker(bind=engine)
    session = make_session()

    cities_with_states = (
                        session.query(City, State)
                        .join(State, City.state_id == State.id)
                        .order_by(City.id)
                        .all()
                        )
    for city, state in cities_with_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
