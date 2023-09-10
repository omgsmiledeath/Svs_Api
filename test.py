import sqlite3
from datetime import datetime

con = sqlite3.connect("./app/app.db")
cur = con.cursor()

#cur.execute("INSERT INTO user(name,password,token) VALUES ('Admin','Admin','token')")
cur.execute("DELETE FROM entry where id=3")
con.commit()