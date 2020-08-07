# импорт библиотек
import pandas as pd
import numpy as np
import os
import copy
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import utils

path_to_data = "C:/Users/Pavel/Documents/Keras"

# Считываем данные из файла
df = pd.read_excel(os.path.join(path_to_data, "Task2_TITANIC_DATA.xlsx"), sheet_name=0)

# Переименовываем столбцы
new_name = ["pclass", "sex", "age", "sibsp", "ticket", "nationality", "parch", "fare", "survived"]
df_new_columns = copy.deepcopy(df)
df_new_columns.columns = new_name

# Удаляем столбец номер билета и гражданство, так как они вряд ли имеет предсказательную силу
df_new_columns.drop(['ticket', 'nationality'], axis=1, inplace=True)

# Вводим дополнительные расчетные столбцы / удаляем уже ненужные фичи
df_new_columns['family'] = df_new_columns['parch'] + df_new_columns['sibsp']
df_new_columns.drop(['parch', 'sibsp'], axis=1, inplace=True)
df_new_columns['is_alone'] = np.where(df_new_columns.family == 0, 1, 0)

# Кодируем фичи
dict_pclass = {'люкс': 1, 'комфорт': 2, 'эконом': 3}
dict_sex = {'мужской': 1, 'женский': 2}
df_new_columns['pclass'] = df_new_columns['pclass'].map(dict_pclass)
df_new_columns['sex'] = df_new_columns['sex'].map(dict_sex)

# Разбиваем возраст пассажиров Титаника на категории
cut_labels_age = [x for x in range(1, 9)]
cut_bins_age = [x for x in range(0, 90, 10)]
df_new_columns['age_'] = pd.cut(df_new_columns['age'], bins=cut_bins_age, labels=cut_labels_age)
df_new_columns.drop(['age'], axis=1, inplace=True)
df_new_columns.rename(columns={'age_': 'age'}, inplace=True)

# Разбиваем тариф пассажиров Титаника на категории, перед этим избавимся от нулевых значений, заменив их средними по классу
for i in [1, 2, 3]:
    df_new_columns.loc[(df_new_columns['pclass'] == i) & (df_new_columns['fare'] == 0), ['fare']] = \
        round(df_new_columns[(df_new_columns['pclass'] == i) & (df_new_columns['fare'] != 0)]['fare'].mean(), 2)

cut_labels_fare = [x for x in range(1, 12)]
cut_bins_fare = [x for x in range(0, 600, 50)]
df_new_columns['fare_'] = pd.cut(df_new_columns['fare'], bins=cut_bins_fare, labels=cut_labels_fare)
df_new_columns.drop(['fare'], axis=1, inplace=True)
df_new_columns.rename(columns={'fare_': 'fare'}, inplace=True)

# Разбиваем данные на учебную и тестовую выборку
X = df_new_columns.drop(['survived'], axis=1)
y = df_new_columns['survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Нейронная сеть
classifier = Sequential()
classifier.add(Dense(units=32, kernel_initializer='uniform', activation='relu', input_dim=6))
# classifier.add(Dense(units=12, kernel_initializer='uniform', activation='relu'))
# classifier.add(Dense(units=6, kernel_initializer='uniform', activation='relu'))
classifier.add(Dense(units=1, kernel_initializer='uniform', activation='sigmoid'))
classifier.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# Выполняем обучение на тренировочных данных
classifier.fit(X_train, y_train, batch_size=128, epochs=100)

# Определяем точность модели
score = classifier.evaluate(X_test, y_test)
print(score)

# Альтернативный вариант определения точности модели
prediction = classifier.predict(X).tolist()
y_prediction = pd.Series(prediction)
df_new_columns['y_prediction'] = y_prediction
df_new_columns['y_prediction'] = df_new_columns['y_prediction'].str.get(0)

series = []
for val in df_new_columns['y_prediction']:
    if val >= 0.5:
        series.append(1)
    else:
        series.append(0)
df_new_columns['final_y_prediction'] = series

rigth_prediction = df_new_columns[df_new_columns['survived'] == df_new_columns['final_y_prediction']].shape[0]
all_prediction  = df_new_columns.shape[0]
print(round(rigth_prediction/all_prediction, 4))
