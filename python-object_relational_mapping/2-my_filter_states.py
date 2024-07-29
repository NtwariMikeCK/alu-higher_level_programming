#!/usr/bin/python3
"""mysql"""

import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Connects to a MySQL database and starting with 'N', sorted by id.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.
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
    # Execute the query to get states with names starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)
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
    Entry point of the script. Expects exactly 3 arguments:
    mysql username, mysql password, and database name.
    """
    # Check if there are exactly 3 arguments (script name + 3 arguments)
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>")
    else:
        # Extract arguments from command line
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        # Call the function to filter and list states
        filter_states(username, password, database)
