#!/usr/bin/python3
"""Module that contains the definition of the State class and an instance Base."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class that represents the states table in the database."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
