#!/usr/bin/python3
"""Defines the State model with a relationship to City.

This module defines the State class, mapped to the MySQL table
`states`, including a one-to-many relationship to City. Deleting
a State cascades to delete all of its linked City objects.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state stored in the `states` MySQL table.

    Attributes:
        id (int): The primary key, auto-generated and unique.
        name (str): The name of the state, up to 128 characters.
        cities (list): Related City objects, deleted in cascade
            when this State is deleted.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan"
    )
