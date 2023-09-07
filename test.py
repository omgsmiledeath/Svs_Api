import sqlite3


con = sqlite3.connect("./app/app.db")
cur = con.cursor()

cur.execute("INSERT INTO entry (date,owner,desc) values ('2023-09-07-12-00-00','я','железо')")

con.commit()