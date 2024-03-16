#!/usr/bin/python3
"""retrieves rows from the 'states' table based on a provided term to find"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    db_connexion = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                   db=argv[3], host='localhost', port=3306)
    cursor = db_connexion.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;""")
    db_all_rows = cursor.fetchall()
    for row in db_all_rows:
        print(row)
    db_connexion.close()
