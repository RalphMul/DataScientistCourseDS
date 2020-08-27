"""
author: Ralph Mul
date: 14-08-2020
file: fruit_accuracy.py
version: 0.1
description: this code is written during the Coursera course fundamentals of Machine Learning. It is used to validate the accuracy as made by our ai model
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import cm

#import the data
fruits = pd.read_table('readonly/fruit_data_with_colors.txt')

# For this example, we use the mass, width, and height features of each fruit instance
X = fruits[['mass', 'width', 'height']]
y = fruits['fruit_label']

# default is 75% / 25% train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

"""

n_neigbors = 5
knn = KNeighborsClassifier(n_neighbors = 5)
"""
 # we choose 5 nearest neighbors

from sklearn.neighbors import KNeighborsClassifier
k_range = range(1,20)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))

plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(k_range, scores)
plt.xticks([0,5,10,15,20]);
plt.show()
