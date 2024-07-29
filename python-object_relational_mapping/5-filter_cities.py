#!/usr/bin/python3
import MySQLdb
import sys

def filter_cities(username, password, database, state_name):
    """
    Connects to a MySQL database and lists all cities from the specified state.
    The results are sorted by city id and are SQL injection safe.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.
        state_name (str): The name of the state to filter cities by.
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the query using parameterized inputs to prevent SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    
    # Fetch all rows from the executed query
    cities = cursor.fetchall()
    
    # Extract city names from the results
    city_names = [city[0] for city in cities]
    
    # Print the results as a comma-separated list
    print(", ".join(city_names))
    
    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    """
    Entry point of the script. Expects exactly 4 command-line arguments:
    mysql username, mysql password, database name, and state name. If the number of
    arguments is incorrect, prints a usage message.
    """
    # Check if there are exactly 4 arguments (script name + 4 arguments)
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py")
        print("       <mysql username>")
        print("       <mysql password>")
        print("       <database name>")
        print("       <state name>")
    else:
        # Extract arguments from command line
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        # Call the function to filter and list cities
        filter_cities(username, password, database, state_name)
