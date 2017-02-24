#-*- coding:utf-8 -*-

import sqlite3 as lite

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description): d[col[0]] = row[idx]
    return d

def get_data(db, query):
    con = lite.connect(db)
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows  

if __name__ == "__main__":
    db = 'test.db'
    query = "SELECT * FROM Cars;"
    data = get_data(db, query)
    for row in data : 
        print (row)

