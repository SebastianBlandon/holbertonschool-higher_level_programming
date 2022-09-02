#!/usr/bin/python3
"""
 Filter states by user input
 Write a script that takes in an argument and displays
 all values in the states table of hbtn_0e_0_usa where
 name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cmd = """SELECT id, name
         FROM states
         WHERE name='{}'
         ORDER BY id ASC""".format(sys.argv[4])
    cur.execute(cmd)
    nStates = cur.fetchall()

    for state in nStates:
        if (state[1] == sys.argv[4]):
            print(state)

    cur.close()
    db.close()
