# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:34:55 2017

@author: NKLSTAC
"""
import numpy as np
import matplotlib.pyplot as plt

def subordinating_degree(u):
    A = []
    for data in u:      
        if(data < 0):
            A.append(0)
        else:
            A.append(1/(1+100/data**2))
    return A
    
def complementary(A):
    C=[]
    for data in A:
        C.append(1 - data)
    return C

def union(A, B):
    if(len(A) == len(B)):
        res=[]
        for d1, d2 in zip(A, B):
            res.append(max(d1, d2))
        return res
    else:
        return []

u = np.linspace(-100, 100, 1000)

A = subordinating_degree(u)
A_C = complementary(A)
U = union(A, A_C)

plt.figure(1)
plt.plot(u, A, 'r')
plt.figure(2)
plt.plot(u, A_C, 'b')
plt.figure(3)
plt.plot(u, U, 'y')