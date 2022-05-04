import sqlite3
import random

conn = sqlite3.connect('/home/pavel/Документы/crontab/db_cron.sqlite')
cur = conn.cursor()

#cur.execute("CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, val INTEGER NOT NULL);")

current_val = random.randint(1,100)
cur.execute("INSERT INTO data(val) values(?);",(current_val,))

conn.commit()
cur.close()
conn.close()