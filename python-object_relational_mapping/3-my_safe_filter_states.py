#!/usr/bin/python3
"""Script that safely lists all states matching a user-provided name.

This module connects to a MySQL server using MySQLdb and prints
every row in the `states` table whose `name` matches the given
argument, ordered by `id` in ascending order. The query uses a
parameterized statement to protect against SQL injection.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (state_name,)
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
