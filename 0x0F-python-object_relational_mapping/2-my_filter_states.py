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
    cur.execute(f"SELECT * FROM states \
            WHERE CONVERT( `name` USING Latin1) \
            COLLATE Latin1_General_CS = '{sys.argv[4]}' ORDER BY `id` ASC;"
    states = cur.fetchall()

    for state in states:
        print(state)
