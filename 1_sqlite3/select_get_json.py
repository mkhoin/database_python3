#-*- coding:utf-8 -*-

import sqlite3 as lite

def get_data(db, query):
    con = lite.connect(db)
    cur = con.cursor()
    cur.executescript(query)
    rows = cur.fetchall()
    return rows  

if __name__ == "__main__":
    con


with con :
    con.row_factory = lite.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM Cars')
    rows = cur.fetchall()
    for row in rows:
        print('%s %s %s' %(row['Id'], row['Name'], row['Price']))


