#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Ensure there are exactly 3 arguments
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>")
        sys.exit(1)
    
    # Extract arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Create an engine that connects to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session instance
    session = Session()
    
    # Query all State objects and sort them by id
    states = session.query(State).order_by(State.id).all()
    
    # Print the results in the specified format
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()
