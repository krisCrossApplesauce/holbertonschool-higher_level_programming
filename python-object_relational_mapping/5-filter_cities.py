#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def cities_by_state():
    """ does something """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])

    curs = db.cursor()

    comm = "SELECT cities.id, cities.name, states.name\
            FROM cities LEFT JOIN states ON cities.state_id=states.id\
            WHERE state.name = %s ORDER BY cities.id ASC"
    curs.execute(comm, (sys.argv[4],))

    rows = curs.fetchall()
    for r in rows:
        print(r)

    db.close()


if __name__ == "__main__":
    cities_by_state()
