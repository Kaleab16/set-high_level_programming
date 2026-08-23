#!/usr/bin/python3
"""Script that lists all cities with their associated state.

This module connects to a MySQL server using MySQLdb and prints
every row from the `cities` table joined with the `states` table,
ordered by `cities.id` in ascending order.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
