import pygame
grid_width=30
grid_height=30
rows = 10
columns = 10
x_size = grid_width * columns
y_size = grid_height * rows

game_data=[[0 for col in range(columns)] for row in range(rows)]

def draw_rect():
    screen.fill((0,0,0))
    snake_color=(255,0,0)
    for r in range(rows):
        for c in range(columns):
            if game_data[r][c]>=1:
                pygame.draw.rect(screen,snake_color,pygame.Rect(r * grid_height,c * grid_width, grid_width, grid_height))
                        
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
    
    # handle FPS
    clock.tick(20)          
                
# close and exit
pygame.display.quit()
pygame.quit()
exit()