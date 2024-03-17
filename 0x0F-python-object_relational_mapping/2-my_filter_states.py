#!/usr/bin/python3
"""
A script to takes in an argument, displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3])

    cur = database.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{:s}'\
            ORDER BY states.id ASC".format(argv[4]))

    result = cur.fetchall()

    for state in result:
        print(state)

    cur.close()
    database.close()
