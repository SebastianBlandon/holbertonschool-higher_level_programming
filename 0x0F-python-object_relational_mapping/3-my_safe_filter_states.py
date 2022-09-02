#!/usr/bin/python3
"""
 SQL Injection...
 Wait, do you remember the previous task?
 Did you test "Arizona'; TRUNCATE TABLE states ;
 SELECT * FROM states WHERE name = '" as an input?
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
         WHERE name=%s
         ORDER BY id ASC"""
    cur.execute(cmd, (sys.argv[4],))
    nStates = cur.fetchall()

    for state in nStates:
        print(state)

    cur.close()
    db.close()
