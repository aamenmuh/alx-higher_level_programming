#!/usr/bin/python3
"""
Main function to filter states by name
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC;", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        if (state != states[len(states) - 1]):
            print(state, end=", ")
        else:
            print(state)
