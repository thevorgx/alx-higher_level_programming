#!/usr/bin/python3
"""First state model"""

from sqlalchemy import MetaData, Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base(metadata=MetaData())


class State(Base):
    """classe State"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade="all, delete-orphan")
