#!/usr/bin/python3
"""
A script that lists all states with a name  hbtn_0e_0_usa.

The script takes three arguments: MySQL username, name.
It connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )
    # Create a cursor to execute SQL queries
    cursor = db.cursor()
    # Execute the SQL query to find states with names starting with 'N'
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    # Fetch all the results and print them
    states = cursor.fetchall()
    for state in states:
        print(state)
    # Close the cursor and database connection
    cursor.close()
    db.close()
