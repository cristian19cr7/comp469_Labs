# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:05:19 2020

@class: COMP469
@author: Cristian Aguilar
@Title: Lab 7: tictactoe minimax
"""
import numpy as np
from copy import deepcopy

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.utility = -99
        self.minORmax = 0 # 1 max -1 min
        self.gameOver = False
        self.size = 1
        
        
def gameover(board):
    if(board[1][1] != ' '):
        if(board[0][0] == board[1][1] == board[2][2]):
            if(board[0][0] == 'X'):
                return (True, 1)
            else:
                return (True, -1)
        elif(board[0][2] == board[1][1] == board[2][0]):
            if(board[0][2] == 'X'):
                return (True, 1)
            else:
                return (True, -1)
        
    if(board[0][0] == board[0][1] == board[0][2] and board[0][0] != ' '):
        if(board[0][0] == 'X'):
            return (True, 1)
        else:
            return (True, -1)
    elif(board[1][0] == board[1][1] == board[1][2] and board[1][0] != ' '):
        if(board[1][0] == 'X'):
            return (True, 1)
        else:
            return (True, -1)
    elif(board[2][0] == board[2][1] == board[2][2] and board[2][0] != ' '):
        if(board[2][0] == 'X'):
            return (True, 1)
        else:
            return (True, -1)
    elif(board[0][0] == board[1][0] == board[2][0] and board[0][0] != ' '):
        if(board[0][0] == 'X'):
            return (True, 1)
        else:
            return (True, -1)
    elif(board[0][1] == board[1][1] == board[2][1] and board[0][1] != ' '):
        if(board[0][1] == 'X'):
            return (True, 1)
        else:
            return (True, -1)
    elif(board[0][2] == board[1][2] == board[2][2] and board[0][2] != ' '):
        if(board[0][2] == 'X'):
            return (True, 1)
        else:
            return (True, -1)
    #checking for a tie
    emptySpots = 0
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '):
                emptySpots+=1
    
    if(emptySpots == 0):
        return (True, 0)
    
    return (False, -99)


def getMin(data):
    minimum = data[0].utility
    if(len(data) == 1):
        return minimum
    for i in data:
        if(minimum > i.utility):
            minimum = i.utility
    return minimum

def getMax(data):
    maximum = data[0].utility
    if(len(data) == 1):
        return maximum
    
    for i in data:
        if(maximum < i.utility):
            maximum = i.utility
    return maximum

def nextMove(board, fringe, parent):
    arrBoard = []
    tempBoard = deepcopy(board)
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '):
                tempBoard = deepcopy(board)
                if(parent.minORmax == 1):
                    tempBoard[i][j] = 'X'
                else:
                    tempBoard[i][j] = 'O'
                tempNode = Node(tempBoard)
                tempval = gameover(tempBoard)
                tempNode.gameOver = tempval[0]
                tempNode.utility = tempval[1]
                tempNode.parent = parent
                if(parent.minORmax == 1):
                    tempNode.minORmax = -1
                elif(parent.minORmax == -1):
                    tempNode.minORmax = 1
                if(tempNode.gameOver == False):
                    fringe.append(tempNode)
                arrBoard.append(tempNode)
    return arrBoard

def ContructTheTreeUsingBFS(node):
    fringe = [node]
    
    while(len(fringe) != 0):
        nextNode = fringe.pop(0)
        tempchild = nextMove(nextNode.data, fringe, nextNode)
        if(tempchild != []):
            nextNode.children = tempchild
            root.size += len(tempchild)
    
    
def minimax(node):
    if(node.utility == -99):
        for child in node.children:
            minimax(child)
    
    currParent = node.parent
    if(currParent == None): #at the root
        bestChoose = None
        for i in node.children:
            if(i.gameOver == True and node.utility == i.utility):
                print(np.matrix(i.data), '\n')
                return
            elif(node.utility == i.utility):
                bestChoose = i
        print(np.matrix(bestChoose.data), '\n')
        return
    for child in currParent.children:
        if(child.utility == -99):
            return
        
    if(currParent.minORmax == -1):# min
        currParent.utility = getMin(currParent.children)
    elif(currParent.minORmax == 1): # max
        currParent.utility = getMax(currParent.children)
            
        
        
start = [[' ', ' ', ' '],
         [' ', 'X', 'O'],
         ['X', 'O', ' ']]
root = Node(start)
root.minORmax = 1
ContructTheTreeUsingBFS(root)
minimax(root)




















