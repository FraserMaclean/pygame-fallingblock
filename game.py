import pygame
import time
from random import seed
from random import randint
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Falling Blocks")

x = 225
y = 100
width = 50
height = 50
vel = 10

ex = randint(0,500)
ey = 400
ewidth = 50
eheight = 50
evel = 5
    
def drawShapes():
    window.fill((0,0,0))
    pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    pygame.draw.rect(window, (255, 0, 0), (ex, ey, ewidth, eheight))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(50)

    drawShapes()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if ey > evel:
        ey -= evel

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

pygame.quit()
