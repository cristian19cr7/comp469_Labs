# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:11:54 2020

@author: Cristian Aguilar
"""
import math
import numpy as np

class Node():
    def __init__(self, data,cost,x,y):
        self.data = data
        self.cost = cost
        self.children = []
        self.parent = None
        self.x = x
        self.y = y

def outOfboundsCheck(x, y):
    if(x <=-1 or y <= -1 or x >= 5 or y >= 7):
        return True
    else:
        return False

def eucildean_distance(currX, currY, goalX, goalY):
    x = abs(currX - goalX)
    y = abs(currY - goalY)
    z = x**2 + y**2
    z = math.sqrt(z)
    return z

def manhattan_distance(currX, currY, goalX, goalY):
    x = abs(currX - goalX)
    y = abs(currY - goalY)
    return x + y

def nextInTheFringe(fringeList):
    closestIndex = 0
    closest = fringeList[closestIndex]
    for index in range(0, len(fringeList), 1):
        if(fringeList[index].cost < closest.cost):
            closestIndex = index
            closest = fringeList[closestIndex]
    

    return fringe.pop(closestIndex)

def successor_fcn(currNode, fringeList, visitedList, heuristic):
    
    x = currNode.x
    y = currNode.y
    visitedList.append((x,y))
    #left
    if(not outOfboundsCheck(x, y+1) and graph[x][y+1] != 'x'):
        if((x,y+1) not in visitedList):
            if(heuristic == '1'):
                child = Node(graph[x][y+1], eucildean_distance(x, y+1, 4, 6),x,y+1)
            else:
                child = Node(graph[x][y+1], manhattan_distance(x, y+1, 4, 6),x,y+1)
            child.parent = currNode
            currNode.children.append(child)
            fringeList.append(child)
    #right
    if(not outOfboundsCheck(x, y-1) and graph[x][y-1] != 'x'):
        if((x,y-1) not in visitedList):
            if(heuristic == '1'):
                child = Node(graph[x][y-1], eucildean_distance(x, y-1, 4, 6),x,y-1)
            else:
                child = Node(graph[x][y-1], manhattan_distance(x, y-1, 4, 6),x,y-1)
            child.parent = currNode
            currNode.children.append(child)
            fringeList.append(child)
    #up
    if(not outOfboundsCheck(x-1, y) and graph[x-1][y] != 'x'):
        if((x-1,y) not in visitedList):
            if(heuristic == '1'):
                child = Node(graph[x-1][y], eucildean_distance(x-1, y, 4, 6),x-1,y)
            else:
                child = Node(graph[x-1][y], manhattan_distance(x-1, y, 4, 6),x-1,y)
            child.parent = currNode
            currNode.children.append(child)
            fringeList.append(child)
     
    #down
    if(not outOfboundsCheck(x+1, y) and graph[x+1][y] != 'x'):
        if((x+1,y) not in visitedList):
            if(heuristic == '1'):
                child = Node(graph[x+1][y], eucildean_distance(x+1, y, 4, 6),x+1,y)
            else:
                child = Node(graph[x+1][y], manhattan_distance(x+1, y, 4, 6),x+1,y)
            child.parent = currNode
            currNode.children.append(child)
            fringeList.append(child)
            
def greedy(currentNode, heuristic):
    fringe.append(currentNode)
    nextNode = nextInTheFringe(fringe)
    graphPrint[nextNode.x][nextNode.y] = '*'
    print(np.matrix(graphPrint))
    successor_fcn(nextNode,fringe,visited, heuristic)
    #check goal
    if(nextNode.data == 'G'):
            return nextNode
    
    while fringe != []:
        nextNode = nextInTheFringe(fringe)
        graphPrint[nextNode.x][nextNode.y] = '*'
        print(np.matrix(graphPrint), "\n")
        #check goal
        if(nextNode.data == 'G'):
            return nextNode
        successor_fcn(nextNode,fringe, visited, heuristic)
    
graph = [['S',2,3,1,1,'x',3],
         [1,1,'x','x',3,'x',1],
         [3,1,'x',1,1,1,1],
         [1,1,3,4,4,1,2],
         [1,4,2,1,'x',1,'G']]

graphPrint = [['-','-','-','-','-','-','-'],
              ['-','-','-','-','-','-','-'],
              ['-','-','-','-','-','-','-'],
              ['-','-','-','-','-','-','-'],
              ['-','-','-','-','-','-','-']]
fringe = []
visited = []
root = Node('S', 0, 0,0)

method = input("Which method Eucildean (1) or Manhattan (2) => ")
endNode = greedy(root, method)
print(visited)
if(method == '1'):
    print("ran with Eucildean")
else:
    print("ran with Manhattan")








