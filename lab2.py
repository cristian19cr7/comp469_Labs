# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:26:37 2020
@class:comp 469
@author: Cristian Aguilar
@Title: Lab2
"""
import string
import queue


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
        result.append(node.data)
        for i in range(0, len(curr.children1)):
            if(result[0] == start and result[len(result) - 1] == end):
                return result
            else:
                findPath(start, end, curr.children1[i])
                
        if(result[0] == start and result[len(result) - 1] == end):
            return result
        else:
            result.remove(node.data)
            
        

dictonary = ["toy", "cop","try","coy","fry","cry","bay","lay","boy","bow","cup", "fey"]

startState = "boy"
GoalState = "cup"
result = []
fringe = queue.Queue()
fringe.put(startState)
done = False
treeRoot = Tree(Node(startState))
dictonary.pop(dictonary.index(startState))
currentNode = treeRoot.root
currentNode.addNode1(childernFinder(startState, dictonary))

fringe.get()
for i in range(0, len(currentNode.children1)):
    fringe.put(currentNode.children1[i].data)
                
currLen = len(currentNode.children1)
currentNode = currentNode.children1
index = 1
while (not done):
    for j in range(0, len(currentNode)):
        for i in range(0, currLen):
            childNode = currentNode[i]
            childNode.addNode1(childernFinder(childNode.data, dictonary))
            for i in range(0, len(childNode.children1)):
                fringe.put(childNode.children1[i].data)
                
            if(childNode.data == GoalState):
                temp = treeRoot.root
                print("From:", startState, "to:", GoalState)
                print("result:", findPath(startState, GoalState, temp))
                print("fringe:", list(fringe.queue))
                done = True
                break
            else:
                fringe.get()
        if done:
            break
        if(j >= len(currentNode)):
            currentNode = treeRoot.root.children1[index].children1
            index += 1
            continue
        
        currentNode = currentNode[j].children1
        currLen = len(currentNode)
        
    index -= 1
    currentNode = treeRoot.root.children1[index].children1
    index += 1




    
    









