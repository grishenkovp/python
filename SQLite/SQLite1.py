import sqlite3
import pandas as pd

con = sqlite3.connect("C:\\Users\\Pavel\\Documents\\database.db")
cur = con.cursor()
# **********************************************************************************************************************
sql_create_tabl = """\
CREATE TABLE regions (id_region INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, code_region INTEGER);
CREATE TABLE sales (id_sale INTEGER PRIMARY KEY AUTOINCREMENT,region INTEGER,value INTEGER);
"""
try:
    cur.executescript(sql_create_tabl)
except sqlite3.DatabaseError as err:
    print("Ошибка:", err)
else:
    print("Таблицы успешно созданы")
# ***********************************************************************************************************************
arr_regions = [("north", 1000), ("south", 1000), ("west", 2000), ("east", 2000)]
arr_sales = [(1, 100), (3, 200), (4, 500), (2, 1000), (1, 1000)]

sql_insert_regions = """\
INSERT INTO regions (name,code_region) VALUES(?,?)
"""
sql_insert_sales = """\
INSERT INTO sales (region,value) VALUES(?,?)
"""

try:
    cur.executemany(sql_insert_regions, arr_regions)
except sqlite3.DatabaseError as err:
    print("Таблица Регионы. Ошибка:", err)
else:
    print("Таблица Регионы. Данные успешно добавлены")
    con.commit()

try:
    cur.executemany(sql_insert_sales, arr_sales)
except sqlite3.DatabaseError as err:
    print("Таблица Продажи. Ошибка:", err)
else:
    print("Таблица Продажи. Данные успешно добавлены")
    con.commit()
# **********************************************************************************************************************
cur.execute("SELECT r.name, s.value FROM sales as s LEFT OUTER JOIN regions as r ON s.region=r.id_region")
df_old = cur.fetchall()
df = pd.DataFrame(df_old, columns=['regions','value'])
print(df)
# **********************************************************************************************************************
cur.close()
con.close()
