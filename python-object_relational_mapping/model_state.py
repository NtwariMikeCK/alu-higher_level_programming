#!/usr/bin/python3
"""
This module defines a State class and links it to the MySQL table 'states'.
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()


class State(Base):
    """
    State class to map to the 'states' table in MySQL.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sys import argv
    # Create an engine that connects to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}
                            @localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Create all tables in the database (in this case, just 'states')
    Base.metadata.create_all(engine)
