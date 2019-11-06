#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:53:37 2019

@author: zsll
"""

import pygame
import random
grid_width=30
grid_height=30
rows = 30
columns = 30
x_size = grid_width * columns
y_size = grid_height * rows

#food
white=(255,255,255)

game_data=[[0 for col in range(columns)] for row in range(rows)]
game_data[2][2]=1
game_data[2][3]=2
game_data[2][4]=3

def getSnakeHead() :
    for r in range(rows):
        for c in range(columns):
            if game_data[r][c] == 1:
                new_r=r
                new_c=c
                return new_r,new_c
 
def updateData(length_snake):
    for r in range(len(game_data)):
        for c in range(len(game_data[r])):
            game_data[r][c] += 1
            if game_data[r][c]==1:
                game_data[r][c]=0
            if  game_data[r][c]>length_snake:   
                game_data[r][c]=0

direction=0
def make_sure_the_direc():
    global direction
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:direction=1
    if pressed[pygame.K_DOWN]:direction=2
    if pressed[pygame.K_LEFT]:direction=3
    if pressed[pygame.K_RIGHT]:direction=4
    return direction

def move_snake(direction): #1:up 2:down 3:left 4:right
    if getSnakeHead() is not  None:
        new_r,new_c=getSnakeHead()
        direction=make_sure_the_direc()
        if direction == 1:
            new_r -= 1
        elif direction == 2:
            new_r += 1
        elif direction == 3:
            new_c -= 1
        else:
            new_c +=1
        updateData(6)
        game_data[new_r][new_c] = 1   
    return game_data

length_snake=6
food_x=0
food_y=0
def find_food():
    global length_snake
    global food_x
    global food_y
    new_r,new_c=getSnakeHead()
    print(new_r,new_c,food_x,food_y)
    if food_x==new_r and food_y ==new_c:
        length_snake +=1
        food_x = random.randrange(0, columns)
        food_y = random.randrange(0, rows)  
        print(food_x, food_y)
        print("the snake is " + str(length_snake))
    return length_snake

def draw_rect():
    screen.fill((0,0,0))
    snake_color=(255,0,0)
    for r in range(rows):
        for c in range(columns):
            if game_data[r][c]>=1:
                pygame.draw.rect(screen,snake_color,pygame.Rect(c * grid_height,r * grid_width, grid_height, grid_width))
    pygame.draw.rect(screen,white,(food_y * grid_height,food_x * grid_width, 30, 30))     
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((x_size, y_size))

done = False
clock= pygame.time.Clock()
while not done:
    # handle events
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = True
        
    # Draw the game
    draw_rect()
    #call the function
    getSnakeHead()
    move_snake(direction)
    find_food()
    # handle FPS
    clock.tick(100)          
                
# close and exit
pygame.display.quit()
pygame.quit()
exit()

