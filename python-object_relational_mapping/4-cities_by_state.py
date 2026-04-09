#!/usr/bin/python3
"""
this code shows cities and states table's data
with using join
"""


import sys
import MySQLdb

if __name__ == "__main__":
    username, password, name = sys.argv[1:]
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=name,
            port=3306
    )
    c = db.cursor()
    c.execute(
            "SELECT cities.id, cities.name, states.name"
            "FROM cities JOIN states ON cities.state_id"
            "ORDER BY cities.id"
        )
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
