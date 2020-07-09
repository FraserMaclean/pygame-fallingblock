import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Falling Blocks")

x = 225
y = 100
width = 50
height = 50
vel = 10

def drawPlayerCharacter():
    window.fill((0,0,0))
    pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    drawPlayerCharacter()

pygame.quit()
