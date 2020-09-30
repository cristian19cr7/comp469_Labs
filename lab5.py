# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:11:54 2020

@author: Cristian Aguilar
"""
import math
from scipy.spatial import distance

def eucildean_distance(currX, currY, goalX, goalY):
    x = abs(currX - goalX) - 1
    print(x)
    y = abs(currY - goalY) - 1
    print(y)
    z = x**2 + y**2
    z = math.sqrt(z)
    return z

def manhattan_distance(currX, currY, goalX, goalY):
    x = abs(currX - goalX)-1
    y = abs(currY - goalY)-1
    return x + y
    
graph = [['S',2,3,1,1,'x',3],
         [1,1,'x','x',3,'x',1],
         [3,1,'x',1,1,1,1],
         [1,1,3,4,4,1,2],
         [1,4,2,1,'x',1,'G']]




print(eucildean_distance(0,0, 6,6))

print(manhattan_distance(0,0,6,6))









