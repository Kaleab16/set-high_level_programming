#!/usr/bin/python3
"""Script that lists all State objects with their City objects.

This module connects to a MySQL server using SQLAlchemy and prints
every State, followed by each of its cities indented on the next
lines, using a single database query via eager loading of the
`cities` relationship. Results are sorted by `states.id` and then
`cities.id`.
"""
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).options(
        joinedload(State.cities)
    ).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        cities = sorted(state.cities, key=lambda c: c.id)
        for city in cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
