#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:22:21 2019

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
 
def getSnakeHead() :
    for r in range(rows):
        for c in range(columns):
            if game_data[r][c] == 1:
                new_r=r
                new_c=c#+1
                return new_r,new_c
            
def clearData():
    for y in range(len(game_data)):
        for x in range(len(game_data[y])):
            game_data[y][x]=0        

def move_snake(direction): #1:up 2:down 3:left 4:right
    if getSnakeHead() is not  None:
        new_r,new_c=getSnakeHead()
        if direction==1:
            new_r=new_r-1
            new_c=new_c
        elif direction ==2:
            new_r=new_r+1
            new_c=new_c
        elif direction ==3:
            new_r=new_r
            new_c=new_c-1
        else:
            new_r=new_r
            new_c=new_c+1
        clearData()
        game_data[new_r][new_c]=1 
    return game_data
print("the value of new_r,new_c is " + str(getSnakeHead()))
    


print("the new position of head is"+str(getSnakeHead()))
print("game data is: ") 
for row in game_data :
  print(row)

#call the function
getSnakeHead()
#clearData()
move_snake(3)


#see if the output is correct
print("the game data is now :")
for rows in game_data :
  print(rows)