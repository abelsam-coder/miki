import sqlite3
db = sqlite3.connect("database.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS hacked (username TEXT,password TEXT)")
db.commit()