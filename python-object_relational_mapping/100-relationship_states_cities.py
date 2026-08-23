#!/usr/bin/python3
"""Script that creates State "California" with City "San Francisco".

This module connects to a MySQL server using SQLAlchemy and creates
a State named "California" with a linked City named "San Francisco",
using the `cities` relationship to establish the association.
"""
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)

    session.add(new_state)
    session.commit()

    session.close()
