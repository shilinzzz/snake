#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:53:37 2019

@author: zsll
"""

import pygame
grid_width=30
grid_height=30
rows = 10
columns = 10
x_size = grid_width * columns
y_size = grid_height * rows

game_data=[[0 for col in range(columns)] for row in range(rows)]

game_data[2][2]=1

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

def move_snake(): #1:up 2:down 3:left 4:right
    if getSnakeHead() is not  None:
        new_r,new_c=getSnakeHead()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:new_r-=1
        if pressed[pygame.K_DOWN]:new_r+=1
        if pressed[pygame.K_LEFT]:new_c-=1
        if pressed[pygame.K_RIGHT]:new_c+=1
        clearData()
        game_data[new_r][new_c]=1 
    return game_data


def draw_rect():
    screen.fill((0,0,0))
    snake_color=(255,0,0)
    for r in range(rows):
        for c in range(columns):
            if game_data[r][c]>=1:
                pygame.draw.rect(screen,snake_color,pygame.Rect(c * grid_height,r * grid_width, grid_height, grid_width))
                        
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
    # handle movement
    #pressed = pygame.key.get_pressed()
    #if pressed[pygame.K_UP]:y-=10
    #if pressed[pygame.K_DOWN]:y+=10
    #if pressed[pygame.K_LEFT]:x-=10
    #if pressed[pygame.K_RIGHT]:x+=10
    
    # Draw the game
    draw_rect()
    #call the function
    getSnakeHead()
    move_snake()
    # handle FPS
    clock.tick(20)          
                
# close and exit
pygame.display.quit()
pygame.quit()
exit()