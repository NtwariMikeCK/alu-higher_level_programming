#!/usr/bin/python3
"""
This script changes the name of a State object with id = 2 to "New Mexico"
in the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Ensure there are exactly 3 arguments
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>")
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
    
    # Query for the state with id = 2
    state = session.query(State).filter(State.id == 2).first()
    
    # Check if the state exists
    if state:
        # Update the name of the state
        state.name = "New Mexico"
        
        # Commit the transaction to the database
        session.commit()
    
    # Close the session
    session.close()
