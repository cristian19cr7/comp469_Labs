# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 19:40:34 2020

@class: COMP469
@author: Cristian Aguilar
@Title: Homework 2: 8-puzzle A*
"""
import timeit
import numpy as np
import sys
from copy import deepcopy


class Node():
    def __init__(self, data):
        self.data = data
        self.children1 = []
        self.parent = None
        self.cost = 0
        
        
def outOfboundsCheck(x, y):
    if(x <=-1 or y <= -1 or x >= 3 or y >= 3):
        return True
    else:
        return False
def createGoalDictonary(goalMatrix):
    table = {}
    for i in range(0,3):
        for j in range(0,3):
            table[goalMatrix[i][j]] = (i, j)
    return table

def printPath(pathList):
    sys.stdout.flush()
    pathList.reverse()
    for m in pathList:
        print(np.matrix(m),"\n")
        #time.sleep(1)
        sys.stdout.flush()
        
def matrixToNumber(matrix):
    stringNum = ""
    for i in range(0,3):
        for j in range(0,3):
            stringNum += str(matrix[i][j])
    return stringNum
                
def ifGoalState(board, goalState):
    return matrixToNumber(board) == matrixToNumber(goalState)    


def HeuristicFunc(node):
    misplacedTiles = 0
    
    for i in range(0,3):
        for j in range(0,3):
            if(node.data[i][j] != Goal[i][j]):
                misplacedTiles += 1
    node.cost = misplacedTiles
    
    for i in range(0,3):
        for j in range(0,3):
            x = goalDict.get(node.data[i][j])[0]
            y = goalDict.get(node.data[i][j])[1]
            node.cost += abs(x-i) + abs(y-j)
    
    
    

def fringeAndvisitedUpdate(fringeList, visitedList, current_board, current_node):
    key = matrixToNumber(current_board)
    if(key in visitedList):
        return
    else:
        newNode = Node(current_board)
        HeuristicFunc(newNode)
        current_node.children1.append(newNode)    
        newNode.parent = current_node
        fringeList[newNode] = newNode.cost        

def successor_fcn(currNode, fringeList, visitedList):
    currBoard = currNode.data
    x, y = 0, 0
    for i in range(0,3):
        for j in range(0, 3):
            if(currBoard[i][j] == 0):
                x = i
                y = j
                break;

    
    #left
    if(not outOfboundsCheck(x, y+1)):
        child = deepcopy(currBoard)
        child[x][y] = currBoard[x][y+1]
        child[x][y+1] = currBoard[x][y]
        fringeAndvisitedUpdate(fringeList, visitedList, child, currNode)
        #print(child)
        
        
    #down
    if(not outOfboundsCheck(x+1, y)):
        child = deepcopy(currBoard)
        child[x][y] = currBoard[x+1][y]
        child[x+1][y] = currBoard[x][y]
        fringeAndvisitedUpdate(fringeList, visitedList, child, currNode)
        #print(child)
        
        
    #right
    if(not outOfboundsCheck(x, y-1)):
        child = deepcopy(currBoard)
        child[x][y] = currBoard[x][y-1]
        child[x][y-1] = currBoard[x][y]
        fringeAndvisitedUpdate(fringeList, visitedList, child, currNode)
        #print(child)
        
        
    #up
    if(not outOfboundsCheck(x-1, y)):
        child = deepcopy(currBoard)
        child[x][y] = currBoard[x-1][y]
        child[x-1][y] = currBoard[x][y]
        fringeAndvisitedUpdate(fringeList, visitedList, child, currNode)
        #print(child)
        
         
def findPathWithParent(root, endNode):
    curr = endNode
    while curr != None:
        result.append(curr.data)
        curr = curr.parent

def A_star(currentNode):
    print("finding solution...")
    fringe[currentNode] = currentNode.cost
    nextNode = min(fringe.items(), key = lambda x:x[1])
    del fringe[nextNode[0]]
    nextNode = nextNode[0]
    visited[matrixToNumber(nextNode.data)] = 1
    if(ifGoalState(nextNode.data, Goal)):
        return nextNode
    successor_fcn(nextNode, fringe, visited)
    
    while(fringe):
        nextNode = min(fringe.items(), key = lambda x:x[1])
        del fringe[nextNode[0]]
        nextNode = nextNode[0]
        if(ifGoalState(nextNode.data, Goal)):
            print("Goal found")
            return nextNode
        visited[matrixToNumber(nextNode.data)] = 1
        successor_fcn(nextNode, fringe, visited)
    

#test matrices
#Goal = [[7, 2, 4], [0, 6, 1], [5, 8, 3]]
#Goal = [[2, 0, 4], [7, 5, 6], [8, 3, 1]]
#Goal = [[2, 0, 4], [5, 7, 3], [1, 8, 6]]
#Goal = [[2, 1, 0], [3, 4, 5], [6, 7, 8]] #<--- this one STILL doesnt work IDK why 

start = timeit.default_timer()
Board = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
Goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
#to get the index of any number from the matrix when calculating the manhattan distances
goalDict = createGoalDictonary(Goal)
fringe = {}
visited= {}
result = []
start = timeit.default_timer()
root = Node(Board)
HeuristicFunc(root)
endNode = A_star(root)
stop = timeit.default_timer()
if(matrixToNumber(Goal) in visited):
    print("WTF")
findPathWithParent(root, endNode)
printPath(result)
print("h1(n) + h2(n) is the cost for each node")
print("Size of solution path: ", len(result))
print("Size of fringe: ", len(fringe))
print("Number of visited nodes: ", len(visited))
print('Time: ', stop - start, " seconds")




























