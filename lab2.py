# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:26:37 2020

@author: Cristian Aguilar
"""
import string
import sys

class Tree():
    def __init__(self,root):
        self.root = root
        self.children = []
    def addNode(self,obj):
        self.children.append(obj)

class Node():
    def __init__(self, data):
        self.data = data
        self.children1 = []
    def addNode1(self,obj):
        for x in obj:
            self.children1.append(Node(x))

def childernFinder(str1, dictList):
    alpha = string.ascii_lowercase
    result = []
    for i in range(0, len(str1)):
        for j in range(0, len(alpha)):
            temp = list(str1)
            temp[i] = alpha[j]
            strTemp = "".join(temp)
            if(strTemp in dictList and str1 != strTemp):
                result.append(strTemp)
                dictList.pop(dictList.index(strTemp))
    return result

def findPath(start, end, node):
        curr = node
        listResult = []
        fringe.append(node.data)
        for i in range(0, len(curr.children1)):
            if(fringe[0] == start and fringe[len(fringe) - 1] == end):
                listResult = fringe
                return listResult
            else:
                findPath(start, end, curr.children1[i])
                
        if(fringe[0] == start and fringe[len(fringe) - 1] == end):
            listResult = fringe
            return listResult
        else:
            fringe.remove(node.data)
            
        
"""use a list to push the entries in until the node hits a leaf node, then check 
 if the start and end of the list is correct if so return the list else continue to iterate through
 https://medium.com/basecs/breaking-down-breadth-first-search-cebe696709d9
"""

dictonary = ["try", "toy", "cop","cup","coy","fry","cry","bay","lay","boy","bow","fey"]

startState = "boy"
GoalState = "cup"
fringe = []
done = False
treeRoot = Tree(Node(startState))
dictonary.pop(dictonary.index(startState))
currentNode = treeRoot.root

currentNode.addNode1(childernFinder(startState, dictonary))
#print(currentNode.children1[2].data)
currLen = len(currentNode.children1)
index = 0


currentNode = currentNode.children1

while (not done):
    for j in range(0, len(currentNode)):
        for i in range(0, currLen):
            childNode = currentNode[i]
            print(childNode.data)
            childNode.addNode1(childernFinder(childNode.data, dictonary))
            if(childNode.data == GoalState):
                ##path finder function call
                temp = treeRoot.root
                print(findPath(startState, "try", temp))
                done = True
                sys.exit()
        currentNode = currentNode[j].children1
        currLen = len(currentNode)
    






"""while (not done):
    for i in range(0, currLen):
        childNode = currentNode.children1[i]
        print(childNode.data)
        childNode.addNode1(childernFinder(childNode.data, dictonary))
        if(childNode.data == GoalState):
            ##path finder function call
            done = True
            break
    currentNode = currentNode.children1
    currLen = len(currentNode)
"""



    
    









