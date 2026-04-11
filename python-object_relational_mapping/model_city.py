#!/usr/bin/python3
"""
this codes create new table with using sqlalchemy
orm method
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    this class represents City table
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, Foreignkey('states.id'))
