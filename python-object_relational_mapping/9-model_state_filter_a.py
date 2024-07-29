#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Ensure there are exactly 3 arguments
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <mysql username> <mysql password> <database name>")
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
    
    # Query for State objects that contain the letter 'a' in the name
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    
    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()
