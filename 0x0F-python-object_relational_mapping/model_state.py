#!/usr/bin/python3
"""
Defines a State model.

This module contains the SQLAlchemy State class, representing a state entity
linked to the MySQL table 'states'. It inherits from the SQLAlchemy Base.

Note:
    The State model is designed for use in a MySQL database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        Represents a state for a MySQL database.
        Attributes:
            id (int): Represents the unique identifier (primary key) of
                      the state.
            name (str): Represents the name of the state, with a maximum
                        length of 128 characters.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
