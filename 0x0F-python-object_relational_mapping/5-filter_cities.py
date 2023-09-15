#!/usr/bin/python3
"""a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3]
    )
    cur = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id WHERE states.name = %s"
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join([row[1] for row in query_rows]))
    cur.close()
    conn.close()
