#!/usr/bin/python3
"""
This script adds a new State object “Louisiana” to the database hbtn_0e_6_usa
and prints the new state's id.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Ensure there are exactly 3 arguments
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>")
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
    
    # Create a new State object
    new_state = State(name="Louisiana")
    
    # Add the new State object to the session
    session.add(new_state)
    
    # Commit the transaction to the database
    session.commit()
    
    # Print the id of the newly created State object
    print(new_state.id)
    
    # Close the session
    session.close()
