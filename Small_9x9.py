# -*- coding: utf-8 -*-
"""

@author: barengific
"""

import numpy as np

grid = np.array([[5,3,0,0,7,0,0,0,0],
                 [5,0,0,1,9,5,0,0,0],
                 [0,9,8,0,0,0,0,6,0],
                 
                 [8,0,0,0,6,0,0,0,3],
                 [4,0,0,8,0,3,0,0,1],
                 [7,0,0,0,2,0,0,0,6],
                 
                 [0,6,0,0,0,0,2,8,0],
                 [0,0,0,4,1,9,0,0,5],
                 [0,0,0,0,8,0,0,7,9]])

# if zero then it is infilled

r,c = grid.shape

# search every cell in grid (rows then columns)
# if empty (zero) is found then search the same row and column
# insert a no repeating number
# keep array of possible values to try

def cellCheck(array,rows,cols,proposed):
    rek = 0
    cek = 0
    
    state = False
    #normalise numbers
    if rows == 2 or rows == 5 or rows == 8:
        rek = rows-1
    if rows == 3 or rows == 6 or rows == 9:
        rek = rows-2   
    
    if cols == 2 or cols == 5 or cols == 8:
        cek = cols-1 
    if cols == 3 or cols == 6 or cols == 9:
        cek = cols-2
    
    #cell = array[rows,cols]
    
    #check dups in column
    for i in range(r):
        if array[rows,i] == proposed:
            print('dup found')
            state == False
            return
        else:
            state == True
    
    #check dups in row
    for j in range(r):
        if array[j,cols] == proposed:
            print('dup found')
            state == False
            return 
        else:
            state == True    
    
    # #check dups in local grid
    for k in range(rek,rek+2):
        if array[k,cols] == proposed:
            print('dup found')
            state == False
            return
        else:
            state == True   
        
    for n in range(cek,cek+2):
        if array[rows,n] == proposed:
            print('dup found')
            state == False
            return  
        else:
            state == True   
    #####
    #####
    #####   3x3 local search
    ##### search local grid
    #### search local grid    
    
    if state == True:
        grid[rows,cols] = proposed
        
    return 

#cellCheck(grid,2,2,12)

def starts():
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
    


for i in range (100):
    starts()

     
 