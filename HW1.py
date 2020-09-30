# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 12:00:45 2020

@class: COMP469
@author: Cristian Aguilar
@Title: Homework 1: 8-puzzle BFS
"""
import timeit
from copy import deepcopy

class Node():
    def __init__(self, data):
        self.data = data
        self.children1 = []
        self.parent = None
        
        
def outOfboundsCheck(x, y):
    if(x <=-1 or y <= -1 or x >= 3 or y >= 3):
        return True
    else:
        return False

def printPath(pathList):
    for m in pathList:
        for i in range(0,3):
            for j in range(0,3):
                print(m[i][j]," ", end = '')
            print("")
        print("\n")
        
def matrixToNumber(matrix):
    stringNum = ""
    for i in range(0,3):
        for j in range(0,3):
            stringNum += str(matrix[i][j])
    return stringNum
                
def ifGoalState(board, goalState):
    return board == goalState    

def fringeAndvisitedUpdate(fringeList, visitedList, current_board, current_node):
    key = matrixToNumber(current_board)
    if(key in visitedList):
        return
    else:
        newNode = Node(current_board)
        current_node.children1.append(newNode)
        newNode.parent = current_node
        fringeList.append(newNode)
        

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
        
        
    #right
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


def BFS():
    print("finding solution...")
    if(ifGoalState(root.data, Goal)):
        return findPathWithParent(root, root)
    
    fringe.append(root)
    
    while(fringe != []):
        node = fringe.pop(0)
        visited[matrixToNumber(node.data)] = 1
        successor_fcn(node, fringe, visited)
        for child in node.children1:
            if(matrixToNumber(child.data) not in visited):
                if(ifGoalState(child.data, Goal)):
                    return child
                
    print("Error: fringe empty????")
        
       
#test matrices
#Goal = [[7, 2, 4], [0, 6, 1], [5, 8, 3]]
#Goal = [[2, 0, 4], [7, 5, 6], [8, 3, 1]]
#Goal = [[2, 0, 4], [5, 7, 3], [1, 8, 6]]
#Goal = [[2, 1, 0], [3, 4, 5], [6, 7, 8]] <--- this one doesnt work IDK why 

start = timeit.default_timer()
Board = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
Goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
fringe = []
visited= {}
result = []
root = Node(Board)
endNode = BFS()
if(matrixToNumber(Goal) in visited):
    print("WTF")
findPathWithParent(root, endNode)
printPath(result)
print("Size of fringe: ", len(fringe))
print("Number of visited nodes: ", len(visited))
stop = timeit.default_timer()
print('Time: ', stop - start)





























