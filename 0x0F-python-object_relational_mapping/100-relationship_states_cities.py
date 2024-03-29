#!/usr/bin/python3
"""add a state and a city, the state can have a city attribute"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                         argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    make_session = sessionmaker(bind=engine)
    session = make_session()
    state_name = State(name='California')
    city_name = City(name='San Francisco')
    state_name.cities.append(city_name)
    session.add(state_name)
    session.add(city_name)
    session.commit()
