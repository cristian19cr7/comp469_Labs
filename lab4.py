# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:41:55 2020

@class: COMP469
@author: Cristian Aguilar
@Title: Lab 4
"""

from queue import PriorityQueue
class Node():
    def __init__(self, data,cost):
        self.data = data
        self.cost = cost
        self.children = []
        self.parent = None


def outOfboundsCheck(x, y):
    if(x <=-1 or y <= -1 or x >= 3 or y >= 3):
        return True
    else:
        return False

def successor_fcn(currNode, fringeList, visitedList):
    visitedList.append(currNode.data)
    x, y = 0, 0
    child = currNode
    for i in range(0,3):
        for j in range(0,3):
            if(graph[i][j] == currNode.data):
                x, y = i, j
                break
    #left
    if(not outOfboundsCheck(x, y - 1)):
        if graph[x][y-1] not in nodeFringe:
            child = Node(graph[x][y-1], dict_cost.get(graph[x][y-1]))
            child.parent = currNode
            currNode.children.append(child)
            fringe.put((child.cost, child.data))
            nodeFringe[child.data] = child
            
    #right
    if(not outOfboundsCheck(x, y + 1)):
        if graph[x][y+1] not in nodeFringe:
            child = Node(graph[x][y+1], dict_cost.get(graph[x][y+1]))
            child.parent = currNode
            currNode.children.append(child)
            fringe.put((child.cost, child.data))
            nodeFringe[child.data] = child
    #up
    if(not outOfboundsCheck(x - 1, y)):
        if graph[x-1][y] not in nodeFringe:
            child = Node(graph[x-1][y], dict_cost.get(graph[x-1][y]))
            child.parent = currNode
            currNode.children.append(child)
            fringe.put((child.cost, child.data))
            nodeFringe[child.data] =  child
    #down
    if(not outOfboundsCheck(x + 1, y)): 
        if graph[x+1][y] not in nodeFringe:
            child = Node(graph[x+1][y], dict_cost.get(graph[x+1][y]))
            child.parent = currNode
            currNode.children.append(child)
            fringe.put((child.cost, child.data))
            nodeFringe[child.data] = child

def goal_test(curr_loc, goal_loc):
    return curr_loc == goal_loc
    

def extract_plan(current_node, endNode):
    current_node = endNode
    while current_node != None:
        result.append(current_node.data)
        current_node = current_node.parent
        
    return result.reverse()

def UCS(currentNode):
    nodeFringe[currentNode.data] = currentNode
    successor_fcn(currentNode , fringe, visited)
    currkey = fringe.get()[1]
    curr = nodeFringe[currkey]

    while not fringe.empty():
        
        successor_fcn(curr, fringe, visited)
        currkey = fringe.get()[1]
        curr = nodeFringe[currkey]
        if(goal_test(curr.data, goal)):
            return curr
        
        
    return curr
        
        

graph = [['S', 'a', 'b'],['c','d','e'],['f','h','G']]
dict_cost = {'S':0,'a':1,'b':1,'c':2,'d':2,'e':3,'f':3,'h':3,'G':1}
start = 'S'
goal = 'G'
fringe = PriorityQueue()
nodeFringe = {}
visited = []
result = []
root = Node(start, dict_cost.get(start))



goalNode = UCS(root)
extract_plan(root, goalNode)
print(result)
print("visited: ", visited)

