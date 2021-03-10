import pandas as pd
import numpy as np
import openpyxl
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)
pd.set_option('display.width', 0)

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
# from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
# import xgboost
from sklearn.metrics import accuracy_score

# **********************************************************************************************************************

# Считываем исходные датасеты
path_old = 'C:/Users/Pavel/Downloads/dataset1.xlsx'
file_old = pd.read_excel(path_old, sheet_name='Sheet1')
df_old = file_old
# print(df_old.info())

path_new = 'C:/Users/Pavel/Downloads/dataset2.xlsx'
file_new = pd.read_excel(path_new, sheet_name='Sheet1')
df_new = file_new
# print(df_new.info())

# Переименовываем столбцы в датасетах
name_dict = {'Кол-во негаб. накладных': 'bill_outsize_count', 'Кол-во логинов на сайт ДЛ': 'log_count',
                       'Коэф. лояльности':'k_loyalty','Средний процент скидки':'discount_%',
                       'Доля экспресс-доставки':'express_delivery_%','Среднее кол-во накладных в мес.':'bill_count',
                       'Средний оборот':'amount','Доля доставки до адреса':'delivery_address_%',
                       'Коэф-т отзывчивости':'k_responsiveness','Коэф. разнообразия типов услуг':'k_diversity_service',
                       'Среднее кол-во жалоб':'complaint_count','Категория клиента через месяц':'category_client',
                       'ОПФ':'status'}
df_old = df_old.rename(columns=name_dict)
df_new = df_new.rename(columns=name_dict)
# print(df_new)

#Кодируем status в двух датафреймах
status_dict = {'ЮЛ': 0, 'ФЛ': 1}
df_old['status'] = df_old['status'].map(status_dict)
df_new['status'] = df_new['status'].map(status_dict)
# print(df_old['status'].value_counts())

# Нормализуем данные по оборотам в двух датасетах
df_old['amount'] = (df_old['amount'] - df_old['amount'].min())/(df_old['amount'].max()-df_old['amount'].min())
df_old['bill_outsize_count'] = (df_old['bill_outsize_count'] - df_old['bill_outsize_count'].min())/(df_old['bill_outsize_count'].max()-df_old['bill_outsize_count'].min())
df_old['log_count'] = (df_old['log_count'] - df_old['log_count'].min())/(df_old['log_count'].max()-df_old['log_count'].min())
df_old['bill_count'] = (df_old['bill_count'] - df_old['bill_count'].min())/(df_old['bill_count'].max()-df_old['bill_count'].min())
df_old['k_responsiveness'] = (df_old['k_responsiveness'] - df_old['k_responsiveness'].min())/(df_old['k_responsiveness'].max()-df_old['k_responsiveness'].min())
df_old['complaint_count'] = (df_old['complaint_count'] - df_old['complaint_count'].min())/(df_old['complaint_count'].max()-df_old['complaint_count'].min())


df_new['amount'] = (df_new['amount'] - df_new['amount'].min())/(df_new['amount'].max()-df_new['amount'].min())
df_new['bill_outsize_count'] = (df_new['bill_outsize_count'] - df_new['bill_outsize_count'].min())/(df_new['bill_outsize_count'].max()-df_new['bill_outsize_count'].min())
df_new['log_count'] = (df_new['log_count'] - df_new['log_count'].min())/(df_new['log_count'].max()-df_new['log_count'].min())
df_new['bill_count'] = (df_new['bill_count'] - df_new['bill_count'].min())/(df_new['bill_count'].max()-df_new['bill_count'].min())
df_new['k_responsiveness'] = (df_new['k_responsiveness'] - df_new['k_responsiveness'].min())/(df_new['k_responsiveness'].max()-df_new['k_responsiveness'].min())
df_new['complaint_count'] = (df_new['complaint_count'] - df_new['complaint_count'].min())/(df_new['complaint_count'].max()-df_new['complaint_count'].min())
# df_old['amount'].hist()
# plt.show()

#  Выводим корреляционную матрицу. Высокая степень корреляции между двумя признаками значит,
# что мы можем исключить один из них, так как они содержат одну и ту же информацию.
# corr = df_old.corr()
# print(corr)

# Выделяем массив с только нужными фичами и прогнозируемым признаком

X = df_old.drop(['category_client','status','bill_outsize_count'], axis=1)
X_new = df_new.drop(['status','bill_outsize_count'], axis=1)
feature_name = X.columns
y = df_old['category_client']

# Разбиваем данные на учебную и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=11)
# **********************************************************************************************************************
# # Тестируем 5 алгоритмов чтобы отобрать лучший
# list_alg = [SVC(), GaussianNB(), KNeighborsClassifier(), DecisionTreeClassifier(), RandomForestClassifier(n_estimators=200)]
# list_name = ['Метод опорных векторов', 'Наивный Байес', 'K-ближайших соседей', 'Деревья решений', 'Случайный лес']
# for alg, name_alg in zip(list_alg, list_name):
#     model = alg
#     model.fit(X_train, y_train)
#     expected = y_test
#     predicted = model.predict(X_test)
#
#     # Оценка качества алгоритма
#     print('--------------- ' + name_alg + ' ---------------')
#     print(metrics.classification_report(expected, predicted))
#     print(metrics.confusion_matrix(expected, predicted))
#
#     y_train_predict = model.predict(X_train)
#     y_test_predict = model.predict(X_test)
#     err_train = np.mean(y_train != y_train_predict)
#     err_test = np.mean(y_test != y_test_predict)
#     print(round(err_train,2), round(err_test,2))
#
#     accuracy = accuracy_score(y_test, y_test_predict)
#     print("Accuracy: %.2f%%" % (accuracy * 100.0))

# **********************************************************************************************************************
# # По результам теста выбираем Случайный лес и ищем фичи, создающие лишний шум
# #
# model = RandomForestClassifier(n_estimators=200)
# model.fit(X_train, y_train)
# expected = y_test
# predicted = model.predict(X_test)
#
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))
#
# y_train_predict = model.predict(X_train)
# y_test_predict = model.predict(X_test)
# err_train = np.mean(y_train != y_train_predict)
# err_test = np.mean(y_test != y_test_predict)
# print(round(err_train, 2), round(err_test, 2))
#
# accuracy = accuracy_score(y_test, y_test_predict)
# print("Accuracy: %.2f%%" % (accuracy * 100.0))
#
# importances = model.feature_importances_
# indices = np.argsort(importances)[::-1]
# print('Важность фич для прогноза')
# for f, idx in enumerate(indices):
#     print(f+1, feature_name[idx],importances[idx])
# **********************************************************************************************************************
# Предсказываем результаты
model = RandomForestClassifier(n_estimators=200)
model.fit(X, y)
predicted = model.predict(X_new)
df_final = pd.DataFrame(predicted)
df_final.to_excel('C:/Users/Pavel/Downloads/dataset3.xlsx', sheet_name='Результат')
print('--- Запись завершена! ---')
