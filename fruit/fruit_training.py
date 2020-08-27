"""
author: Ralph Mul
date: 14-08-2020
file: fruit_traing.py
version: 0.1
description: this code is written during the Coursera course fundamentals of Machine Learning. It is used for the first couple of assingments to learn to train models
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fruits = pd.read_table('readonly/fruit_data_with_colors.txt')
#print(fruits.head)
lookup_fruit_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))
print(lookup_fruit_name)

# For this example, we use the mass, width, and height features of each fruit instance
X = fruits[['mass', 'width', 'height']]
y = fruits['fruit_label']

# default is 75% / 25% train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# We now going to create a classifie objectr
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)

# Now we are going to train
knn.fit(X_train, y_train)
#print(knn.fit(X_train, y_train))

# Now we are going to test the accuracy of the classifier on future data
knn.score(X_test, y_test)
#print(knn.score(X_test, y_test))

# Now we are going to predict
# first example: a small fruit with mass 20g, width 4.3 cm, height 5.5 cm
fruit_prediction = knn.predict([[20, 4.3, 5.5]])
fruitName = lookup_fruit_name[fruit_prediction[0]]
print("first example = " + str((fruitName)))
print()


# second example: a larger, elongated fruit with mass 100g, width 6.3 cm, height 8.5 cm
fruit_prediction = knn.predict([[100, 6.3, 8.5]])
fruitName = lookup_fruit_name[fruit_prediction[0]]
print("second example = " + (fruitName))
