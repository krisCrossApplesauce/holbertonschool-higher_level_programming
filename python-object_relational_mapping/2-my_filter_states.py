#!/usr/bin/python3
"""
write a script that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys


def my_filter_states():
    """ does something """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    curs = db.cursor()

    curs.execute(f"SELECT * FROM states WHERE name LIKE BINARY\
                 '{sys.argv[4]}' ORDER BY id ASC")
    rows = curs.fetchall()
    for r in rows:
        print(r)

    db.close()


if __name__ == "__main__":
    my_filter_states()
