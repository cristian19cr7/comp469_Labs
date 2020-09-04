# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 10:26:37 2020

@author: Cristian Aguilar
"""
import string

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



dictonary = ["try", "toy", "cop","cup","coy","fry","cry","bay","lay","boy","bow","fey"]

startState = "boy"
GoalState = "cup"
fringe = []
done = False
treeRoot = Tree(Node(startState))
fringe.append(startState)
currentNode = treeRoot.root

currentNode.addNode1(childernFinder(startState, dictonary))
#print(currentNode.children1[2].data)
currentNode = currentNode.children1[0]
currentNode.addNode1(childernFinder(currentNode.data, dictonary))


    
    









