#!/usr/bin/python3

"""
this python code shows us state table's data
"""
import sys
import MySQLdb

if __name__ == "__main__":
    usernamedb = sys.argv[1]
    passworddb = sys.argv[2]
    namedb = sys.argv[3]
    db = MySQLdb.connect(
            host = "localhost",
            user = usernamedb,
            passwd = passworddb,
            db = namedb,
            port = 3306
    )
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
