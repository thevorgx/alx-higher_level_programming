#!/usr/bin/python3
"""retrieves name and id from the 'cities' table and join them in the
'state' table where cities states id = states id and print the cities
that match the state given as argv[4]"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    db_connexion = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                   db=argv[3], host='localhost', port=3306)
    state_to_find = argv[4]
    cursor = db_connexion.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;""")
    db_all_rows = cursor.fetchall()
    city_names = []
    for row in db_all_rows:
        if row[2] == state_to_find:
            city_names.append(row[1])
    require_output = ", ".join(city_names)
    print(require_output)
    db_connexion.close()
