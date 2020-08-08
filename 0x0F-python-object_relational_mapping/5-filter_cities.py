#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that statve
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
    db_cursor.execute("SELECT cities.name FROM cities JOIN states ON " +
                      "cities.state_id = states.id WHERE states.name=%s " +
                      "ORDER BY cities.id ASC", (sys.argv[4],))
    cities = db_cursor.fetchall()
    print(", ".join([city[0] for city in cities]))
    db_cursor.close()
    database.close()
