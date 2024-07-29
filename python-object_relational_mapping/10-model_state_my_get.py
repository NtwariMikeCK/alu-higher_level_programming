#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Ensure there are exactly 4 arguments
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)
    
    # Extract arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
    # Create an engine that connects to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database), pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session instance
    session = Session()
    
    # Query for the State object with the specific name
    state = session.query(State).filter(State.name == state_name).first()
    
    # Print the result
    if state:
        print(state.id)
    else:
        print("Not found")
    
    # Close the session
    session.close()
