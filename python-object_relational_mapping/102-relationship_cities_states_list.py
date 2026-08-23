#!/usr/bin/python3
"""Script that lists all City objects with their State.

This module connects to a MySQL server using SQLAlchemy and prints
every City, followed by the name of its associated State, using a
single database query via eager loading of the `state` relationship.
Results are sorted by `cities.id` in ascending order.
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

    cities = session.query(City).options(
        joinedload(City.state)
    ).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
