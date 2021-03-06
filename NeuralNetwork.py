# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 11:01:05 2017

BP implenation

@author: OneTree
"""

import numpy as np

# 添加工具函数
def tanh(x):
    return np.tanh(x)
def tanh_deriv(x):
    return 1.0 - pow(tanh(x), 2)
def logistic(x):
    return 1/(1 + np.exp(-x))
def logistic_deriv(x):
    return logistic(x)*(1-logistic(x))

# 神经网络主类
class NeuralNetwork:
    def __init__(self, layers, activation='tanh'):
        """
        :param layers: 一个list，包含每层的单元数目，至少含有两个值
        :param activation: 一个str，指明使用哪个激活函数。可以是'logistic'或'tanh'
        """
        # 选择激活函数
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_deriv
        elif activation == 'tanh':   
            self.activation = tanh
            self.activation_deriv = tanh_deriv
        # 初始化权重容器,[-0.25,0.25]。？此处的处理有疑问
        self.weights = []
        for i in range(1, len(layers) - 1): # 除了输出层
            self.weights.append((2*np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1)*0.25) # layers[i-1]行，layers[i]列
#             self.weights.append((2*np.random.random((layers[i] + 1, layers[i + 1] + 1)) - 1)*0.25)
        self.weights.append((2*np.random.random((layers[len(layers) - 2] + 1, layers[len(layers) - 1])) - 1)*0.25)
#         print(self.weights, len(self.weights))
    def fit(self, X, y, learning_rate = 0.2, epochs = 10000): # X:行数是实例数，列数是维度
        """
        :param learning_rate: 反向修正weights和bias时的系数
        :param epochs: 抽取X中的数据对神经网络进行更新，利用循环次数停止训练
        """
        X = np.atleast_2d(X) # X化为numpy二维数据
        temp = np.ones([X.shape[0], X.shape[1] + 1]) # 初始化全1矩阵,多的列用来添加bias
        temp[:, 0:-1] = X # 在输入层添加bias
        X = temp
        y = np.array(y) # y化为numpy的array
#         print(X, '\n', y)
        # 神经网络训练
        for k in range(epochs): # 共epochs次循环,每次从样本中随机抽样一个
            i = np.random.randint(X.shape[0]) # 随机取一行
            a = [X[i]]
            for l in range(len(self.weights)): # a[l]是在利用上一层计算下一层节点；这里把bias也融入到了weight中，仔细思考可以看明白
#                 print(l, a[l])
                a.append(self.activation(np.dot(a[l], self.weights[l])))
            error = y[i] - a[-1]
            deltas = [error * self.activation_deriv(a[-1])] # 误差
            # 反向更新weights和bias
            for l in range(len(a) - 2, 0, -1):
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_deriv(a[l]))
            deltas.reverse()
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)
    def predict(self, x):
        """
        :param x: 用来测试的样本
        """
        x = np.array(x)
        temp = np.ones(x.shape[0] + 1)
        temp[0:-1] = x
        a = temp
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a