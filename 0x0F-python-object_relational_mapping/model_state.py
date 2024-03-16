#!/usr/bin/python3
from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base(metadata=MetaData())


class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
