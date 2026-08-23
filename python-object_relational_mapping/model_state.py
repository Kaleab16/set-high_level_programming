#!/usr/bin/python3
"""Defines the State model for SQLAlchemy ORM mapping.

This module defines the State class, mapped to the MySQL table
`states`, along with the declarative Base used for ORM mapping.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state stored in the `states` MySQL table.

    Attributes:
        id (int): The primary key, auto-generated and unique.
        name (str): The name of the state, up to 128 characters.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
