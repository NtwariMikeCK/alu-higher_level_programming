#!/usr/bin/python3

"""i hate python"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to a MySQL database and lists all states sorted by id.

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
    # Execute the query to get all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
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
    Entry point of the script. Expects exactly 3 command-line arguments:
    mysql username, mysql password, and database name. If the number of
    arguments is incorrect, prints a usage message.
    """
    # Check if there are exactly 3 arguments (script name + 3 arguments)
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py")
        print("       <mysql username>")
        print("       <mysql password>")
        print("       <database name>")
    else:
        # Extract arguments from command line
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        # Call the function to list states
        list_states(username, password, database)
