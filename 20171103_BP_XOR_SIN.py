# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:07:00 2017

BP test

@author: OneTree
"""

import numpy as np
import NeuralNetwork as nn
import matplotlib.pyplot as plt

# =============================================================================
# # XOR problem
# X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Y = np.array([0, 1, 1, 0])
# 
# bpNN = nn.NeuralNetwork([2, 5, 1])
# 
# print("Begin training with NeuralNetwork...")
# bpNN.fit(X, Y, 0.1, 100)
# print("Training over~")
# 
# print("testing...")
# for sample in X:
#     print(sample, "%f" % bpNN.predict(sample))
# =============================================================================


# SIN problem
X_init = np.linspace(0, np.pi, 30)
Y = np.sin(X_init)
X = X_init.reshape((30, 1))
plt.plot(X_init, Y, '--', linewidth = 2)

bpNN = nn.NeuralNetwork([1, 30, 1])

print("Begin training with NeuralNetwork...")
bpNN.fit(X, Y, 0.1, 50000)
print("Training over~")

print("testing...")
Y0 = np.array([])
for sample in X:
    res = bpNN.predict(sample)
    Y0 = np.append(Y0, res)
    print(sample, "%f" % res)
plt.plot(X_init, Y0, '--', linewidth = 2)
