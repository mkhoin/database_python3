#-*- coding:utf-8 -*-

# Table info is included in "Query script"
def create_table(db, query):
    try :
        import sqlite3 as lite
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
            CREATE TABLE IF NOT EXISTS %s (id INT, Name TEXT, Price INT);
            """ %table
    print (create_table(db, query))

