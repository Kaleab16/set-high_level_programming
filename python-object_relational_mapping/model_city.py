#!/usr/bin/python3
"""Defines the City model for SQLAlchemy ORM mapping.

This module defines the City class, mapped to the MySQL table
`cities`, linked to the `states` table via a foreign key.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represents a city stored in the `cities` MySQL table.

    Attributes:
        id (int): The primary key, auto-generated and unique.
        name (str): The name of the city, up to 128 characters.
        state_id (int): Foreign key referencing the owning state.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
