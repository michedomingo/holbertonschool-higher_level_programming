#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
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
    db_cursor.execute("SELECT cities.id, cities.name, states.name FROM " +
                      "cities JOIN states ON cities.state_id = states.id " +
                      "ORDER BY cities.id ASC")
    cities = db_cursor.fetchall()
    for city in cities:
        print(city)
    db_cursor.close()
    database.close()
