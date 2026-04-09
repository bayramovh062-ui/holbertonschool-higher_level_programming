#!/usr/bin/python3
"""
this code shows cities and states table's data
with using join
"""


import sys
import MySQLdb

if __name__ == "__main__":
    username, password, name, state_name = sys.argv[1:]
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=name,
            port=3306
    )
    c = db.cursor()
    c.execute(
            "SELECT cities.name "
            "FROM cities JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id", (state_name,)
        )
    rows = c.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))
    c.close()
    db.close()
