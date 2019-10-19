import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))

done = False
is_red=True
x=30
y=30
clock= pygame.time.Clock()
while not done:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_red = not is_red
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:y-=1
    if pressed[pygame.K_DOWN]:y+=1
    if pressed[pygame.K_LEFT]:x-=1
    if pressed[pygame.K_RIGHT]:x+=1
    
    screen.fill((0,0,0))
    if is_red :
        color=(255,0,0)
    else:
        color=(0,128,0)
    pygame.draw.rect(screen,color,pygame.Rect(x,y,60,60))
    pygame.display.flip()
    clock.tick(60)

# close and exit
pygame.display.quit()
pygame.quit()
exit()