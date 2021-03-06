# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZpOVhpcdlYIESAOxMOdqBIoo5rZzLz88

#SUPPORT VECTOR REGRESSION(SVR)

#IMPORTING THE LIBRARIES
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""#READING THE DATASET"""

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
Y = dataset.iloc[:, -1].values
print(X)
print(Y)

"""#RESHAPING THE DEPENDENT VARIABLE BEFORE APPLYING THE FEATURE SCALING"""

Y = Y.reshape(len(Y),1)
print(Y)

"""#FEATURE SCALING"""

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
X = sc_x.fit_transform(X)
Y = sc_y.fit_transform(Y)
print(X)
print(Y)

"""#TRAINING THE SVR MODEL ON THE WHOLE DATASET"""

from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X,Y)

"""#PREDICTING THE RESULTS"""

sc_y.inverse_transform(regressor.predict(sc_x.transform([[6.5]])))

"""#VIZUALIZING THE SVR RESULT"""

plt.scatter(sc_x.inverse_transform(X),sc_y.inverse_transform(Y),color = 'red')
plt.plot(sc_x.inverse_transform(X),sc_y.inverse_transform(regressor.predict(X)),color = 'blue')
plt.title("POSITION VS SALARY(SVR)")
plt.xlabel("POSITION")
plt.ylabel("SALARY")
plt.show()