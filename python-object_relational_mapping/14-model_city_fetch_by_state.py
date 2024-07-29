#!/usr/bin/python3
"""
Fetch and display all City objects from the database hbtn_0e_14_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and join with State to get state names
    cities = session.query(City).join(State).order_by(City.id).all()

    # Display the results
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
