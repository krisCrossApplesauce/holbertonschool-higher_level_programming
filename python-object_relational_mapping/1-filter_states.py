#!/usr/bin/python3
"""
write a script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def filter_states():
    """ does something """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%'
                ORDER BY states.id ASC")
    rows = cur.fetchall()
    for r in rows:
        print(r)

    db.close()


if __name__ == "__main__":
    filter_states()
