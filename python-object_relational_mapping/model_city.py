#!/usr/bin/python3
"""
Define the City class that links to the cities table in the database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """City class to map to the 'cities' table in the database."""
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Define relationship to State
    state = relationship("State", back_populates="cities")

# Add this to model_state.py to establish the relationship
# In model_state.py:
# from sqlalchemy.orm import relationship
# from model_city import City
#
# class State(Base):
#     __tablename__ = 'states'
#     ...
#     cities = relationship("City", back_populates="state")
