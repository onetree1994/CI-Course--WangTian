# -*- coding: utf-8 -*-
"""
Spyder Editor

Perception initial parameters' effect.

This is a temporary script file.
"""

import numpy as np

# weight and bias original value
w = np.array([-1, -1, 0])
# learn rate
iota = 0.01
# data matrix
data1 = np.array([[2, 1, -1], [2, 2, -1], [3, 2, -1]])
data2 = np.array([[4, 0, -1], [5, 0, -1], [5, 1, -1]])

# training
for i in range(1, 1000):
    for d1 in data1:
        w = w - iota*(np.dot(w, d1) - 1)*d1
    for d2 in data2:
        w = w - iota*(np.dot(w, d2) + 1)*d2

# test
print(w)
for d1 in data1:
    print(np.dot(w, d1))
for d2 in data2:
    print(np.dot(w, d2))