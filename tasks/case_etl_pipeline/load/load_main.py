import pandas as pd
import psycopg2
import yaml
import os
from glob import glob
from typing import List
from sql.scripts import create_table_sql, test_table_sql

with open('settings.yaml', encoding='utf8') as f:
    settings = yaml.safe_load(f)

user = settings['DB']['USER']
password = settings['DB']['PASSWORD']
host = settings['DB']['HOST']
post = settings['DB']['PORT']
name = settings['DB']['NAME']

encoding = settings['DATA_TRANSFORM']['ENCODING']
path_data_transform = settings['DATA_TRANSFORM']['PATH']
sep = settings['DATA_TRANSFORM']['SEP']
columns_name = settings['DATA_TRANSFORM']['COLUMNS_NAME']
table_name = settings['DATA_TRANSFORM']['TABLE_NAME']

point = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, post, name)

conn = psycopg2.connect(point)


def create_table(create_table_sql: str = create_table_sql) -> None:
    """Создать таблицу"""
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    cursor.close()
    # conn.close()


def get_all_file(path_data_transform: str = path_data_transform) -> List:
    """Получить список файлов в папке"""
    all_file_name = list(glob(os.path.join(path_data_transform, '*.csv')))
    return all_file_name


def load_data(table_name: str = table_name,
              sep: str = sep,
              columns_name: list = columns_name,
              encoding: str = encoding) -> None:
    """Записать данные в таблицу"""
    cursor = conn.cursor()
    for _ in get_all_file():
        with open(_, 'r', encoding=encoding) as f:
            next(f)
            cursor.copy_from(f, table_name, sep=sep, columns=columns_name)
            conn.commit()
        f.close()
    cursor.close()
    conn.close()


def select_postgresql(sql: str = test_table_sql):
    """Запрос данных из БД"""
    return pd.read_sql(sql, conn)
