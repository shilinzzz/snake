#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:30:20 2019

@author: zsll
"""

grid_width=30
grid_height=30
rows = 10
columns = 10
x_size = grid_width * columns
y_size = grid_height * rows

game_data=[[0 for col in range(columns)] for row in range(rows)]

game_data[3][4]=1  
 
def getNewSnakeHead() :
    for r in range(rows):
        for c in range(columns):
            if game_data[r][c] == 1:
                new_r=r
                new_c=c+1
                return new_r,new_c
            
def clearData():
    for y in range(len(game_data)):
        for x in range(len(game_data[y])):
            game_data[y][x]=0        

def move_snake():
    if getNewSnakeHead() is not  None:
        new_r,new_c=getNewSnakeHead()
        clearData()
        game_data[new_r][new_c]=1 
    return game_data
print("the value of new_r,new_c is " + str(getNewSnakeHead()))
    


print("the new position of head is"+str(getNewSnakeHead()))
print("game data is: ") 
for row in game_data :
  print(row)

#call the function
getNewSnakeHead()
#clearData()
move_snake()
move_snake()

#see if the output is correct
print("the game data is now:")
for rows in game_data :
  print(rows)
 