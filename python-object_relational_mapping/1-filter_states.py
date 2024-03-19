#!/usr/bin/python3
"""
List all the states with the name that start with N
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(port=3304, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%';")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()