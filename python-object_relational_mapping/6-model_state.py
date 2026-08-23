#!/usr/bin/python3
"""Script that creates the `states` table via the State ORM model.

This module connects to a MySQL server using SQLAlchemy and creates
all tables defined by classes inheriting from Base, including the
State class mapped to the `states` table.
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
