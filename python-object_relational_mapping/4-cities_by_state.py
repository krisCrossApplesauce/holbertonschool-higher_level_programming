#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def cities_by_state():
    """ does something """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    curs = db.cursor()

    curs.execute("SELECT cities.id, cities.name, states.name FROM\
                 cities LEFT JOIN states ON cities.state_id=states.id\
                 ORDER BY cities.id ASC")
    rows = curs.fetchall()
    for r in rows:
        print(r)

    db.close()


if __name__ == "__main__":
    cities_by_state()
