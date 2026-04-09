"""
this python code shows us state table's data
"""
import sys
import MySQLdb


usernamedb = sys.argv[1]
passworddb = sys.argv[2]
namedb = sys.argv[3]
db = MySQLdb.connect(
        host = "localhost",
        username = usernamedb,
        password = passworddb,
        database = namedb
)
c = db.cursor()
print(c.execute("SELECT states FROM hbtn_0e_0_usa ORDER BY id"))
