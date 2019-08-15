import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
# from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
# from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
# import xgboost
from sklearn.metrics import accuracy_score
# **********************************************************************************************************************
# Считываем данные из файла 'Продажи'
df_sales = pd.read_csv('D:/.../Sales.csv', sep=';',
                       usecols={'Дата', 'Покупатель', 'Сумма'})
# Переименовываем столбцы
df_sales.rename(columns={'Дата': 'date', 'Покупатель': 'customer_id', 'Сумма': 'amount'}, inplace=True)
# Определяем тип столбцов
# print(df_sales.info())
# Приводим столбцы к нужному типу и упорядочиваем их вывод
df_sales['date'] = pd.to_datetime(df_sales['date'])
df_sales['date_year'] = df_sales['date'].dt.year
df_sales.drop(['date'], axis=1, inplace=True)
df_sales['customer_id'] = df_sales['customer_id'].str.replace('покупатель ', 'customer ')
df_sales['amount'] = df_sales['amount'].str.replace(' ', '')
df_sales['amount'] = df_sales['amount'].str.replace(',', '.')
df_sales['amount'] = pd.to_numeric(df_sales['amount'])
df_sales = df_sales.reindex(['date_year', 'customer_id', 'amount'], axis="columns")
# Группируем данные по году и контрагенту
df_sales = df_sales.groupby(by=['date_year','customer_id'])['amount'].sum()
df_sales = df_sales.reset_index()
# Проводим Pivot для столбца 'date_year'
df_sales = df_sales.pivot(index='customer_id',columns='date_year', values='amount')
df_sales = df_sales.reset_index()
df_sales.columns = ["customer_id", "amount_2016", "amount_2017", "amount_2018"]
df_sales.drop(['amount_2017'], axis=1, inplace=True)
# print(df_sales.columns)
# print(df_sales.info())
# Обрабатываем пропущенные значения
df_sales['amount_2016'] = df_sales['amount_2016'].fillna(df_sales['amount_2016'].mean())
df_sales['amount_2018'] = df_sales['amount_2018'].fillna(df_sales['amount_2018'].mean())
# print(df_sales.info())
# Рассчитываем дополнительную метрику
df_sales["2018_2016"] = (df_sales['amount_2018'] - df_sales['amount_2016']) \
                              / df_sales['amount_2016']
df_sales = df_sales.round(0)
# print(df_sales.head(5))
# **********************************************************************************************************************
# Считываем данные из файла 'Компании'
df_companies = pd.read_csv('D:/.../Companies.csv', sep=';',
                           usecols={'Контрагент', 'Удаленность', 'Уровень конкуренции', 'Длительность контракта',
                                    'Статус'})
# Переименовываем столбцы
df_companies.rename(
    columns={'Контрагент': 'customer_id', 'Удаленность': 'distance', 'Уровень конкуренции': 'competition',
             'Длительность контракта': 'duration', 'Статус': 'status'}, inplace=True)
#
df_companies['customer_id'] = df_companies['customer_id'].str.replace('покупатель ', 'customer ')
status_dict = {'+': 0, '-': 1}
df_companies['status'] = df_companies['status'].map(status_dict)
# print(df_companies.head(5))
# **********************************************************************************************************************
# Считываем данные из файла 'Размер долга'
df_debt = pd.read_csv('D:/.../Debt.csv', sep=';',
                      usecols={'Контрагент', 'Долг'})
# Переименовываем столбцы
df_debt.rename(columns={'Контрагент': 'customer_id', 'Долг': 'debt'}, inplace=True)
# Приводим столбцы к нужному типу
df_debt['customer_id'] = df_debt['customer_id'].str.replace('покупатель ', 'customer ')
df_debt['debt'] = df_debt['debt'].str.replace(',', '.')
df_debt['debt'] = pd.to_numeric(df_debt['debt'])
# print(df_debt.info())
# **********************************************************************************************************************
# Собираем три массива информации в единую таблицу
df_total = pd.merge(df_sales, df_companies, how='outer', on='customer_id')
df_total = pd.merge(df_total, df_debt, how='outer', on='customer_id')
# print(df_total.info())
# Рассчитываем отношение долга к суммарным продажам за 2018 год. Удаляем ненужные столбцы 'amount_2016','amount_2018',
# 'debt', 'customer_id'. Изменяем порядок вывода столбцов
df_total['debt%'] = df_total['debt'] / df_total['amount_2018'] * 100
df_total = df_total.drop(['amount_2016', 'amount_2018', 'debt', 'customer_id'], axis=1)
df_total.rename(columns={'2018_2016': 'sales_growth'}, inplace=True)
df_total = df_total.reindex(['sales_growth', 'debt%', 'distance', 'competition', 'duration', 'status'], axis="columns")
# print(df_total.head(5))
# **********************************************************************************************************************
# Выводим корреляционную матрицу. Высокая степень корреляции между двумя признаками значит,
# что мы можем исключить один из них, так как они содержат одну и ту же информацию.
corr = df_total.corr()
# print(corr)
# **********************************************************************************************************************
X = df_total.drop(['status'], axis=1)
y = df_total['status']
# Проводим нормализацию признаков
X = preprocessing.normalize(X)
# Разбиваем данные на учебную и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
# **********************************************************************************************************************
# Тестируем 4 алгоритма
list_alg = [GaussianNB(), KNeighborsClassifier(), DecisionTreeClassifier(), RandomForestClassifier(n_estimators=200)]
list_name = ['Наивный Байес', 'K-ближайших соседей', 'Деревья решений', 'Случайный лес', 'XGBoost']
for alg, name_alg in zip(list_alg, list_name):
    model = alg
    model.fit(X_train, y_train)
    expected = y_test
    predicted = model.predict(X_test)

    # Оценка качества алгоритма
    print('--------------- ' + name_alg + ' ---------------')
    print(metrics.classification_report(expected, predicted))
    print(metrics.confusion_matrix(expected, predicted))

    y_train_predict = model.predict(X_train)
    y_test_predict = model.predict(X_test)
    err_train = np.mean(y_train != y_train_predict)
    err_test = np.mean(y_test != y_test_predict)
    print(round(err_train,2), round(err_test,2))

    accuracy = accuracy_score(y_test, y_test_predict)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
# **********************************************************************************************************************
# # Подбор оптимальных показателей алгоритма
# # Создаем словарь с параметрами, которые хотим проверить
# params = {"n_estimators": [200], "max_depth": range(5, 10), "min_samples_split": range(5, 10),
#           "min_samples_leaf": range(5, 10)}
# # Cоздаем экземпляр GridSearchCV
# model = RandomForestClassifier()
# search = GridSearchCV(model, params,iid=True, cv=3)
# # Обучаем дерево
# search.fit(X_train, y_train)
# # Сохраняем лучшее дерево по мнению GridSearchCV
# best_tree = search.best_estimator_
# expected = y_test
# predicted = best_tree.predict(X_test)
# # Оценка качества алгоритма
# print('--------------- Случайный лес / Лучшие параметры ---------------')
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))
#
# y_train_predict = best_tree.predict(X_train)
# y_test_predict = best_tree.predict(X_test)
# err_train = np.mean(y_train != y_train_predict)
# err_test = np.mean(y_test != y_test_predict)
# print(err_train, err_test)
