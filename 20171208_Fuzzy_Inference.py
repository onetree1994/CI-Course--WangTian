# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 01:53:56 2017

@author: NKLSTAC
"""
import numpy as np
def isFar(d):
    # membership function of "近"
    d_near = 1-np.fabs(d-0)/100
    # membership function of "远"
    d_far = 1-np.fabs(d-100)/100
    if d_far > d_near:
        return True
    else:
        return False

def isFace(a):
    # membership function of "面向"
    a_face = 1-np.fabs(a-0)/180
    # membership function of "背向"
    a_back = 1-np.fabs(a-180)/180
    if a_face > a_back:
        return True
    else:
        return False

def hasMissile(n):
    # membership function of "无"
    n_null = 0
    if(n == 0):
        n_null = 1
    # membership function of "有"
    n_have = 1-np.fabs(n-10)/10
    if n_have > n_null:
        return True
    else:
        return False

def rules(d, a, n):
    str=""
    print(isFar(d),isFace(a),hasMissile(n))
    if((isFar(d))):
        str="巡航"
    if((not isFar(d)) and isFace(a) and hasMissile(n)):
        str="追击"
    if((not isFar(d)) andaa isFace(a) and (not hasMissile(n)) or (not isFar(d)) and (not isFace(a))):
        str="逃逸"
    print(str)
    
rules(190, 80, 1)
rules(80, 80, 1)
rules(40, 80, 1)
rules(40, 100, 1)
        