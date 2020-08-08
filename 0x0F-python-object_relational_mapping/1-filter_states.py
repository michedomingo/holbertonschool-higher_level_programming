#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
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
    db_cursor.execute("SELECT id, name FROM states WHERE " +
                      "name LIKE BINARY 'N%' ORDER BY id ASC")
    states = db_cursor.fetchall()
    for state in states:
        print(state)
    db_cursor.close()
    database.close()
