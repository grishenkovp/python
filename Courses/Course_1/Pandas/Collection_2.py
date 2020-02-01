import pandas as pd
import numpy as np
import postgresql
import psycopg2
import time
import json
from pprint import pprint


# **********************************************************************************************************************
# Example 15. Чтение денных из БД PostgreSQL. Библиотека postgresql
start_time = time.time()
db = postgresql.open('pq://postgres:admin@localhost:5432/database')
print("Database opened successfully")
records = db.query('Select tb.* From public.tabl as tb')
labels = ['date', 'region', 'product', 'value']
df = pd.DataFrame.from_records(records, columns=labels)
print("Operation done successfully")
print(df)
print("--- %s seconds ---" % (time.time() - start_time))

# Example 16. Чтение данных из БД PostgreSQL. Библиотека psycopg2
start_time = time.time()
conn = psycopg2.connect("dbname='database' user='postgres' password='admin' host='localhost' port='5432'")
print("Database opened successfully")
cursor = conn.cursor()
cursor.execute('Select tb.* From public.tabl as tb')
records = cursor.fetchall()
labels = ['date', 'region', 'product', 'value']
df = pd.DataFrame.from_records(records, columns=labels)
print("Operation done successfully")
cursor.close()
conn.close()
print(df)
print("--- %s seconds ---" % (time.time() - start_time))


# Example 17. Чтение данных из файла JSON. Библиотека Pandas
path = 'dataset/data7.json'
df = pd.read_json(path)
print(df)

# Example 18. Чтение данных с HTML страницы.
# Задаем URL- адрес HTML - файла
url = '...'
df = pd.read_html(url)
print(df)
