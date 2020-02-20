import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df_sales = pd.read_csv("D:/Моя работа/Работа/Python/GitHub/Pandas/Demo_Cohort_analysis/Dataset/Sales.csv", sep=';')
# Выделяем из даты название месяца, удаляем столбец с датами
df_sales['date'] = pd.to_datetime(df_sales['date'], format='%d.%m.%Y')
df_sales['month'] = df_sales['date'].dt.month_name().str.slice(stop=3)
df_sales.drop(['date'], axis=1, inplace=True)
# Задаем новый порядок вывода столбцов
column_titles = ['month', 'region', 'client', 'total_amount']
df_sales = df_sales.reindex(columns=column_titles)
# print(df_sales.head(5))
# Обработка столбца Region. Получаем уникальные значения из столбца и записываем  их в отдельный объект
regions = df_sales['region'].unique()
# Создаем серию, у которой в качестве значений и индексных меток будут выступать уникальные значения
# переменной region, записанные в regions
regions = pd.Series(data=regions, index=regions, name='regions')
# Задаем стоп-слова
stopwrds = set(['г', 'область'])


# Пишем функцию для предобработки значений серии
def clean_region(x):
    wrds = x.replace('.', ' ').split(' ')
    wrds_new = []
    for w in wrds:
        if not w in stopwrds:
            wrds_new.append(w)
    x = ''.join(wrds_new)
    return x


# Применяем функцию к серии
regions = regions.map(clean_region)
# Вносим финальную правку в список регионов
regions['Оренбургская'] = 'Оренбург'
# Заменяем исходные категории переменной region на новые
df_sales['region'] = df_sales['region'].map(regions)
# print(df_sales.head(5))
# Обработка столбца Client. Получаем уникальные значения из столбца и записываем  их в отдельный объект
clients = df_sales['client'].unique()
# Создаем серию, у которой в качестве значений и индексных меток будут выступать уникальные значения
# переменной client, записанные в clients
clients = pd.Series(data=clients, index=clients, name='clients')
# Задаем стоп-слова
stopwrds = set(['ООО', 'ЗАО', 'ИП', 'ОАО'])


# Пишем функцию для предобработки значений серии
def clean_client(x):
    wrds = x.replace('"', ' ').split(' ')
    wrds_new = []
    for w in wrds:
        if not w in stopwrds:
            wrds_new.append(w)
    x = ''.join(wrds_new).capitalize()
    return x


# Применяем функцию к серии
clients = clients.map(clean_client)
# Заменяем исходные категории переменной client на новые
df_sales['client'] = df_sales['client'].map(clients)
# print(df_sales.head(5))
#  Разделим клиентов на две группы: на тех, кто за два месяца совершил больше 10 покупок (группа А) и меньше (группа В)
mask = df_sales['client'].value_counts().lt(10)
df_sales['frequency_sale'] = np.where(df_sales['client'].isin(df_sales['client'].value_counts()[mask].index), 'B', 'A')
# Разделим клиентов на группы по объему закупок за месяц:
df_sales = df_sales.groupby(by=['month', 'client'], as_index=False)['total_amount'].sum()
bins = [0, 10000, 20000, 30000, 40000, np.inf]
group_names = ['E', 'D', 'C', 'B', 'А']
df_sales['size_amount'] = pd.cut(df_sales['total_amount'], bins, right=True, labels=group_names)
print(df_sales)
