#!/usr/bin/python3
"""
same as 2-my_filter_states.py
!!BUT!!
now make it safe from MySQL injections ,'P
"""
import MySQLdb
import sys


def my_safe_filter_states():
    """ does something """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    curs = db.cursor()

    comm = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    curs.execute(comm, (sys.argv[4],))

    rows = curs.fetchall()
    for r in rows:
        print(r)

    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
