# -*- coding: utf-8 -*-
"""

@author: barengific
"""

import numpy as np

grid = np.array([[1,0,0],
                 [0,3,1],
                 [0,0,2]])

# if zero then it is infilled

r,c = grid.shape

# search every cell in grid (rows then columns)
# if empty (zero) is found then search the same row and column
# insert a no repeating number
# keep array of possible values to try

def cellCheck(array,rows,cols,proposed):
    #cell = array[rows,cols]
    for i in range(r):
        if array[rows,i] == proposed:
            print('dup found')
            return array
        
    for j in range(r):
        if array[j,cols] == proposed:
            print('dup found')
            return array
        
    grid[rows,cols] = proposed 
    return array

#cellCheck(grid,2,2,12)
pros = 0

for k in range(r):
    pros+=1
    for i in range(r):
        for j in range(c):
            #possibles = np.empty([0, c])
            if grid[i,j] == 0:
                # try to solve the cell
                print('found zero')
                cellCheck(grid,i,j,pros)
    
            
            
            