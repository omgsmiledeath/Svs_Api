import sqlite3
from datetime import datetime

con = sqlite3.connect("./app/app.db")
cur = con.cursor()

cur.execute("INSERT INTO entry(date,owner,desc) value('')")

con.commit()