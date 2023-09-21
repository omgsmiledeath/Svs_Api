import sqlite3
from datetime import datetime

con = sqlite3.connect("./app/app.db")
cur = con.cursor()

#cur.execute("INSERT INTO user(name,password,token) VALUES ('Admin','Admin','token')")
# for i in range(9,19):
#     cur.execute(f"DELETE FROM entry WHERE id={i}")
# cur.execute("INSERT INTO post (titul,postText,videoUrl,createData,updateData,user) VALUES (?,?,?,?,?,?)",
#             ("First Titul","BLA BLA BLA",
#              "https://youtu.be/lUSFl6sOtpU?si=3_JDWhSYgXFsDlYQ",
#              "",
#              "",
#              "admin"))   
url1 = '<iframe width="560" height="315" src="https://www.youtube.com/embed/lUSFl6sOtpU?si=1aafdDiCKmapzb4R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
url = 'https://www.youtube.com/embed/lUSFl6sOtpU?si=1VlBsQS-89NANkia'

cur.execute("UPDATE post SET videoUrl = ? WHERE id = 1",(url1,))

con.commit()

