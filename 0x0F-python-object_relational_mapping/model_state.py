#!/Users/winniewandia/Workspace/alx-higher_level_programming/0x0F-python-object_relational_mapping/venv/bin/python
"""This module contains the class definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines a class State that links to the MySQL table states.
    It defines the id and name columns of the table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
