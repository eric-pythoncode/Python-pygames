import pygame

pygame.init()

jumping = False
velocity = 0
gravity = 0.5
jumpstrength = -10

width = 600
height = 400
screen = pygame.display.set_mode((width , height))
screencolor = (100,100,100)
pygame.display.set_caption("Move and Jump")

playersize = 50
playercolor = (255, 215, 0)
playerx = (width - playersize) // 2
playery = (height - playersize - 20)
playerspeed = 5

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # keep window open

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerx > 0:
        playerx -= playerspeed
    if keys[pygame.K_RIGHT] and playerx < (width - playersize):
        playerx += playerspeed
    if keys[pygame.K_UP] and playery > 0:
        playery -= playerspeed
    if keys[pygame.K_DOWN] and playery < (height - playersize):
        playery += playerspeed

    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        velocity = jumpstrength

    if jumping:
        playery += gravity
        velocity += gravity
    
    if playery >= height - playersize:
        playery = height - playersize
        jumping = False
        velocity = 0

    screen.fill(screencolor)

    pygame.draw.rect(screen, playercolor, (playerx, playery, playersize, playersize))
    pygame.display.update()
    pygame.time.Clock().tick(60)
pygame.quit()