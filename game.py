import pygame
import random

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width , height))
screencolor = (0,0,0)
pygame.display.set_caption("Python game")

playerwidth = 100
playerheight = 20
playerx = (width - playerwidth) // 2
playery = (height - playerheight - 30)
playercolor = (0, 255, 0)
playerspeed = 5

ballradius = 15
bally = -ballradius
ballx = random.randint(ballradius , width - ballradius)
ballspeed = 5
ballcolor = (255, 215, 0)

score = 0
textcolor = (255, 255, 255)
font = pygame.font.SysFont("Arial", 20)

clock = pygame.time.Clock()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and playerx > 0:
        playerx -= playerspeed
    if keys[pygame.K_RIGHT] and playerx < (width - playerwidth):
        playerx += playerspeed

    bally += ballspeed
    
    if bally > height:
        bally -= ballradius
        ballx = random.randint(ballradius , width - ballradius)

    if (playerx < ballx < playerx + playerwidth) and (playery < bally < ballradius < playery + playerheight):
        score -= 5
        bally = -ballradius
        ballx = random.randint(ballradius , width - ballradius)

    if (playerx < ballx < playerx + playerwidth) and (playery < bally < ballradius < playery + playerheight):
        score += 1
        bally -= ballradius
        ballx = random.randint(ballradius , width - ballradius)
    
    screen.fill(screencolor)
    pygame.draw.rect(screen , playercolor ,(playerx , playery , playerwidth , playerheight))
    pygame.draw.circle(screen , ballcolor , (ballx , bally) , ballradius)

    scoretext = font.render(f"Score: {score}" , True , textcolor)
    screen.blit(scoretext , (10, 10))

    pygame.display.update()

    clock.tick(50)




    

pygame.quit()