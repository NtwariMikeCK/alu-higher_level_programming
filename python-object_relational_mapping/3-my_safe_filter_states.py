#!/usr/bin/python3
"""mysql"""

import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    Connects to a MySQL datnames matching the given state_name,
    sorted by id. This script is safe from SQL injection.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.
        state_name (str): The name of the state to search for.
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
    # Execute the query using parameterized vent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    # Fetch all rows from the executed query
    states = cursor.fetchall()
    # Print the results in the specified format
    for state in states:
        print(state)
    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Entry point of the script. Expects exactly 4 comman arguments:
    mysql username, mysql password, . If the number of
    arguments is incorrect, prints a usage message.
    """
    # Check if there are exactly 4 arguments (script name + 4 arguments)
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py")
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
        # Call the function to filter and list states
        filter_states(username, password, database, state_name)
