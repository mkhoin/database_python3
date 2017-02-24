#-*- coding:utf-8 -*-
import sqlite3 as lite

def create_table(db, query):
    try :
        con = lite.connect(db)
        cur = con.cursor()
        cur.executescript(query)
        con.commit()
    except : 
        return False
    return True

if __name__ == "__main__":
    db = "test.db"
    table = "Cars"
    query = """
            INSERT INTO %s VALUES(3, 'string_text', 34234);
            """ %table
    print (create_table(db, query))


