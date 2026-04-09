#!/usr/bin/python3
"""
this code shows us state table's data but filtered
version with user's input and we will use this input in
the code for find our state name should starting which symbol
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
                "SELECT * FROM states WHERE name LIKE BINARY '{}'"
                "ORDER BY id".format(state_name)
            )
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
