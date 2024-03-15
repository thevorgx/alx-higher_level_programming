#!/usr/bin/python3
"""select states name that starts with 'N' by asc order"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    db_connexion = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                   db=argv[3], host='localhost', port=3306)
    to_find = argv[4]
    cursor = db_connexion.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id;")
    db_all_rows = cursor.fetchall()
    for row in db_all_rows:
        if row[1] == to_find:
            print(row)
    db_connexion.close()
