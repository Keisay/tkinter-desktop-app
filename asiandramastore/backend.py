import sqlite3

def connect():
    conn = sqlite3.connect("dramas.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS drama (id INTEGER PRIMARY KEY, drama text, episodes text, year integer, link text)")
    conn.commit()
    conn.close()
    
def insert(drama, episodes, year, link):
    conn = sqlite3.connect("dramas.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO drama VALUES (NULL,?,?,?,?)", (drama, episodes, year, link))
    conn.commit()
    conn.close()
    
def view():
    conn = sqlite3.connect("dramas.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM drama")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(drama="", episodes="", year="", link=""):
    conn = sqlite3.connect("dramas.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM drama WHERE drama=? OR year=?", (drama, year))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("dramas.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM drama WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
def update(id, drama, episodes, year, link):
    conn = sqlite3.connect("dramas.db")
    cur = conn.cursor()
    cur.execute("UPDATE drama SET drama=?, episodes=?, year=?, link=? WHERE id=?", (drama, episodes, year, link, id))
    conn.commit()
    conn.close()

connect()
#insert("The Break", "John Smith", 1918)

