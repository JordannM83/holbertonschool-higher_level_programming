#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state
"""
import MySQLdb
import sys


def main():
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = %s) ORDER BY cities.id", (sys.argv[4],))
    results = cursor.fetchall()

    cities = [row[0] for row in results]
    print(", ".join(cities))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
