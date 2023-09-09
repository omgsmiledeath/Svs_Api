import sqlite3
from datetime import datetime

con = sqlite3.connect("./app/app.db")
cur = con.cursor()

cur.execute("INSERT INTO user(name,password,token) VALUES ('Admin','Admin','token')")

con.commit()