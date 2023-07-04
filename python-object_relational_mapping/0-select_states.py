#!/usr/bin/python3
"""
write a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def list_states():
    """ does something """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])

    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = curs.fetchall()
    for r in rows:
        print(r)

    db.close()


if __name__ == "__main__":
    list_states()
