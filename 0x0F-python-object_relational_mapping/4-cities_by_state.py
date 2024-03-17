#!/usr/bin/python3
"""
script that lists all cities from the database 
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

    cur.execute("SELECT  cities.id, cities.name, states.name\
            FROM cities JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")

    result = cur.fetchall()

    for city in result:
        print(city)

    cur.close()
    database.close()
