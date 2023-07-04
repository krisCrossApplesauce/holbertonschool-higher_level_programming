#!/usr/bin/python3
"""
write a script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def list_states():
    """ does something """
    db = MySQLdb.connect(host="localhost", user=sys.argv[0], password=sys.argv[1], database=sys.argv[2])

    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id ASC")

    db.close()


if __name__ == "__main__":
    list_states()
