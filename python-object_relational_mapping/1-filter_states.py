#!/usr/bin/python3
"""
this python code shows us all rows which one state's name starting with N
"""
import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        passwd=password,
        user=username,
        port=3306,
        db = name
    )
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
