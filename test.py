import sqlite3
from datetime import datetime

con = sqlite3.connect("./app/app.db")
cur = con.cursor()

#cur.execute("INSERT INTO user(name,password,token) VALUES ('Admin','Admin','token')")
for i in range(9,19):
    cur.execute(f"DELETE FROM entry WHERE id={i}")
cur.execute("INSERT INTO post (titul,postText,videoUrl,createData,updateData,user) VALUES (?,?,?,?,?,?)",
            ("First Titul","BLA BLA BLA",
             "https://youtu.be/lUSFl6sOtpU?si=3_JDWhSYgXFsDlYQ",
             "",
             "",
             "admin"))    
con.commit()

