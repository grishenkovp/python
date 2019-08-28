import numpy as np
import pandas as pd
import sklearn.linear_model as lm
import statsmodels.api as sm
import statsmodels.formula.api as smf

d = {'x1': [3, 5, 3, 3, 5, 2, 1, 5, 5, 3, 5, 3, 3, 5, 2, 1, 5, 5, 3, 5, 3, 3, 5, 2, 1, 5, 5],
     'x2': [9, 5, 3, 9, 10, 6, 1, 15, 15, 9, 5, 3, 9, 10, 6, 1, 15, 15, 9, 5, 3, 9, 10, 6, 1, 15, 15],
     'x3': [1, 3, 2, 3, 2, 2, 1, 2, 2, 1, 3, 2, 3, 2, 2, 1, 2, 2, 1, 3, 2, 3, 2, 2, 1, 2, 2],
     'y': [11, 7, 4, 9, 13, 6, 1, 18, 17, 11, 7, 4, 9, 13, 6, 1, 18, 17, 11, 7, 4, 9, 13, 6, 1, 18, 17]}
df = pd.DataFrame(data=d)
x = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Вариант 1
skm = lm.LinearRegression()
skm.fit(x, y)
print('*****   Вариант 1 ******')
print(skm.intercept_, skm.coef_)

# Вариант 2
results = smf.ols('y ~ x1+x2+x3', data=df).fit()
print('*****   Вариант 2 ******')
print(results.summary())
