#!/usr/bin/python3
"""mysql documentation"""

import MySQLdb
import sys

host="localhost"
port=3306
user=username
passwd=password
db=database


def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host, port, user, passwd, db)
    """Create a cursor object"""
    cursor = db.cursor()
    """Execute the query to get all states sorted by id"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    """Fetch all rows from the executed query"""
    states = cursor.fetchall()
    """Print the results in the specified format"""
    for state in states:
        print(state)    
    """ Close the cursor and database connection"""
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if there are exactly 3 arguments (script name + 3 arguments)
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
    else:
        # Extract arguments from command line
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        # Call the function to list states
        list_states(username, password, database)
