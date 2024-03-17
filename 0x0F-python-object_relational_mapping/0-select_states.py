#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    database = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        password=argv[2],
        port=3306,
        db=argv[3])

    cur = database.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    result = cur.fetchall()
    for state in result:
        print(state)

    cur.close()
    database.close()
