# -*- coding: utf-8 -*-
"""

@author: barengific
"""
import numpy as np

#sdk = np.array([]
sdk = np.array(      [[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])

def setupCells():
    sdk = np.array(      [[5,3,0,0,7,0,0,0,0],
                          [6,0,0,1,9,5,0,0,0],
                          [0,9,8,0,0,0,0,6,0],
                          [8,0,0,0,6,0,0,0,3],
                          [4,0,0,8,0,3,0,0,1],
                          [7,0,0,0,2,0,0,0,6],
                          [0,6,0,0,0,0,2,8,0],
                          [0,0,0,4,1,9,0,0,5],
                          [0,0,0,0,8,0,0,7,9]])
    return sdk

def vnd(row,column,box,number):
    for i in range(1, 9):
        if sdk[row,i] == number:
            #if i in row is number found then....
    for j in range(1,9):
        if sdk[i,column] == number:
            #if i in column is number found then....
            
    #check horizontal
    #check vertical
    #check local box
    
    #return true or false for a cell
    return True
    
#P[:, 1] = [7, 8]

    
print(setupCells())    

    
    
    
    