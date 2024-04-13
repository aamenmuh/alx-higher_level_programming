#!/usr/bin/python3
import sys
import MySQLdb
'''
    main function to list all states
'''
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],passwd=sys.argv[2],db=sys.argv[3])
    
    cur = db.cursor()
    
    states = cur.execute("SELECT * FROM states ORDER BY id")
    
    for state in states:
        print(state)
