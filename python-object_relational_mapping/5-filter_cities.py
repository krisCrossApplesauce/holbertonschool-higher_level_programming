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

    cmnd = "SELECT cities.name FROM cities JOIN states\
            ON cities.state_id = states.id WHERE states.name = %s\
            ORDER BY cities.id ASC"
    curs.execute(cmnd, (sys.argv[4],))

    rows = curs.fetchall()

    for i in range(len(rows)):
        print(rows[i][0], end="")
        if i < len(rows) - 1:
            print("", end=", ")
    print()

    db.close()


if __name__ == "__main__":
    cities_by_state()
