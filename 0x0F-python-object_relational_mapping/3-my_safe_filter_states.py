#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument and safe from MySQL injections
"""
import MySQLdb
import sys

if __name__ == '__main__':
    database = MySQLdb.connect(user=sys.argv[1],
                               password=sys.argv[2],
                               database=sys.argv[3],
                               host='localhost',
                               port=3306)
    db_cursor = database.cursor()
    db_cursor.execute("SELECT id, name FROM states WHERE name=%s " +
                      "ORDER BY id ASC", (sys.argv[4],))
    states = db_cursor.fetchall()
    for state in states:
        print(state)
    db_cursor.close()
    database.close()
