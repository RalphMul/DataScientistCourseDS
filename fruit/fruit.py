"""
author: Ralph Mul
date: 14-08-2020
file: fruit.py
version: 0.1
description: this code is written during the Coursera course fundamentals of Machine Learning. It is used for the first couple of assingments like importing & examing the data
"""

#%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

fruits = pd.read_table('readonly/fruit_data_with_colors.txt')
#print(fruits.head())

# create a mapping from fruit label value to fruit name to make results easier to interpret
lookup_fruit_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))
#print(lookup_fruit_name)

# plotting a scatter matrix
from matplotlib import cm

X = fruits[['height', 'width', 'mass', 'color_score']]
y = fruits['fruit_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
"""
print("The following table is X_train table")
print(X_train)
print()
print("The following table is X_test table")
print(X_test)
print()
print("The following table is y_train table")
print(y_train)
print()
print("The following table is y_test table")
print(y_test)
"""
#now we create a scatter plot
#Please take note that pandas scatter_mattrix needs plotting definition
from matplotlib import cm

cmap = cm.get_cmap('gnuplot')
scatter = pd.plotting.scatter_matrix(X_train, c= y_train, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(9,9), cmap=cmap)
plt.show()

#Now we will create a 3D scatter plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X_train['width'], X_train['height'], X_train['color_score'], c = y_train, marker = 'o', s=100)
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
plt.show()
