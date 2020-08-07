import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from catboost import CatBoostClassifier, CatBoostRegressor, CatBoost

df = pd.read_csv("C:/Users/Pavel/Documents/parkinsons.data.txt")
features = df.loc[:, df.columns != 'status'].values[:, 1:]
labels = df.loc[:, 'status'].values
scaler = MinMaxScaler((-1, 1))
X = scaler.fit_transform(features)
Y = labels
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.14, random_state=7)

model = XGBClassifier()
model.fit(X_train, Y_train)
Y_hat = [round(yhat) for yhat in model.predict(X_test)]
print(accuracy_score(Y_test, Y_hat))
Y_hat = [round(yhat) for yhat in model.predict(X)]
print(accuracy_score(Y, Y_hat))


model = CatBoost()
model.fit(X_train, Y_train)
Y_hat = [round(yhat) for yhat in model.predict(X_test)]
print(accuracy_score(Y_test, Y_hat))
Y_hat = [round(yhat) for yhat in model.predict(X)]
print(accuracy_score(Y, Y_hat))
