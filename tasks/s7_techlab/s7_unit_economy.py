import pandas as pd
from sqlalchemy import create_engine
import yaml
import string

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_colwidth', 50)
pd.set_option('display.expand_frame_repr',False)

with open('settings.yaml', encoding='utf8') as f:
    settings = yaml.safe_load(f)

user = settings['DB']['USER']
password = settings['DB']['PASSWORD']
host = settings['DB']['HOST']
post = settings['DB']['PORT']
name = settings['DB']['NAME']

# path_to_data = "dataset.csv"
# postgresql_table = 'test_tbl'

point_connect = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, post, name)
con = create_engine(point_connect)

# list_usecols = ['request_id', 'cookie', 'view_timestamp', 'search_route', 'departure_date', 'return_date',
#  'trip_type', 'flight', 'flight_route', 'tariff', 'price_total', 'discount', 'booking_number', 'experiment_group']
#
# df = pd.read_csv(path_to_data,usecols=list_usecols)
#
# def processing_string(current_str:str)->str:
#     return current_str.strip()
#
# df['request_id'] = df['request_id'].apply(lambda x:processing_string(x))
#
# df['view_timestamp'] = pd.to_datetime(df['view_timestamp'], format='%d.%m.%Y %H:%M:%S')
# df['departure_date'] = pd.to_datetime(df['departure_date'], format='%m/%d/%Y')

# def parse_date(dt:str):
#         try:
#             return pd.to_datetime(dt, format='%m/%d/%Y')
#         except ValueError:
#             return pd.to_datetime(dt, format='%d.%m.%Y')

# df['return_date'] = df['return_date'].apply(lambda x: str(x).replace('29.02.2022','28.02.2022'))
# df['return_date'] = df['return_date'].apply(lambda dt:parse_date(dt))

# В БД CREATE DATABASE test / CREATE TABLE test_tbl (request_id text, 
#                                                   cookie text,
#                                                   view_timestamp timestamp,
#                                                   search_route text,
#                                                  departure_date date,
#                                                   return_date date,
#                                                   trip_type text,
#                                                   flight text,
#                                                   flight_route text,
#                                                   tariff text,
#                                                   price_total int,
#                                                   discount int,
#                                                   booking_number text,
#                                                   experiment_group int)

# df.to_sql(postgresql_table, point_connect, if_exists='replace', index=False)


def select_postgresql(sql):
    return pd.read_sql(sql, con)

# Отобразить все данные
# sql = '''select tbl.* from test_tbl as tbl'''
# print(select_postgresql(sql))


# Вопрос 1. Сколько посетителей было на сайте за все время
# Строго говоря, по имеющимся данным невозможно точно ответить на данный вопрос, так как cookie не является однозначным
# идентификатором посетителя (клиента). Куки устаревают, пользователи очищают настройки браузеров, могут заходить на
# на сайт с разных устройств и т.д. и т.п. Но так как нет уникальных id клиентов (посетителей), то будем использовать
# поле cookie вместо id.
sql1 = '''select count (distinct tbl.cookie) as total_number_of_clients  from test_tbl as tbl'''
print(select_postgresql(sql1))
print('---------------------')

# Вопрос 2. Какая на сайте конверсия в покупку
# Конверсия в интернет-маркетинге — это отношение числа посетителей сайта, выполнивших на нём какие-либо целевые действия,
# к общему числу посетителей сайта, выраженное в процентах.
sql2 = '''select count(t.*) /
                            (select count (distinct tbl.cookie) as total_number_of_clients  from test_tbl as tbl)
                            * 100 as site_conversion_percent
        from (select tbl.cookie as buying_clients
                        from test_tbl as tbl
                        group by tbl.cookie
                        having sum(tbl.price_total)>0) as t'''
print(select_postgresql(sql2))
print('---------------------')

# Вопрос 3. За каждый день вывести куку пользователя, который первый посетил сайт в течение дня
sql3 = '''with tbl as (select t.dt,
                        first_value(t.cookie) over (partition by t.dt order by t.view_timestamp) as first_value_cookie
                       from (select tbl.cookie,
                                    tbl.view_timestamp,
                                    cast (tbl.view_timestamp as date) as dt
                                    from test_tbl as tbl) as t)
          select t.dt,
                min(t.first_value_cookie) as first_value_cookie
          from tbl as t
          group by t.dt'''
print(select_postgresql(sql3))
print('---------------------')

# Вопрос 4. Посчитать сумму выручки по каждому эксперименту
# Так как в условии прямо не указано, какие именно столбцы нужно задействовать в расчете выручки, то используем
# только поле price_total без учета скидок.
sql4 = '''with tbl as (select tbl.request_id, 
                              tbl.price_total, 
                              tbl.experiment_group,
                             tbl_directory.experiment_group as experiment_group_full
                       from test_tbl as tbl left join
                                                      (select tbl.request_id,
                                                              min(tbl.experiment_group) as experiment_group
                                                       from test_tbl as tbl
                                                       group by tbl.request_id) as tbl_directory 
                                             on tbl.request_id = tbl_directory.request_id)
            select sum(t.price_total) filter (where t.experiment_group_full=1) as group_1,
                   sum(t.price_total) filter (where t.experiment_group_full=2) as group_2          
            from tbl as t'''
print(select_postgresql(sql4))
print('---------------------')