#!/usr/bin/python3

"""
    A Python script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
                         host="localhost", port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            where states.name = %s""", (argv[4], ))
    rows = cursor.fetchall()

    for row in range(len(rows)):
        print(rows[row][0], end='')
        if (row != len(rows) - 1):
            print(end=', ')
        else:
            print()
    cursor.close()
    db.close()
