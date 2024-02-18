#!/usr/bin/python3
"""
script that lists all states with a name starting
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    cur = database.cursor()

    cur.execute("SELECT * FROM  states \
            WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")

    result = cur.fetchall()

    for state in result:
        print(state)

    cur.close()
    database.close()
