import pygame
import sys
import random

pygame.init()

#width height
width, height = 800, 600
screen = pygame.display.set_mode((width,height))

#color
white = (255, 255, 255)
black = (0, 0, 0)
leftpaddlecolor = (0, 255, 0)
rightpaddlecolor = (0, 0, 255)


#define paddle
paddlewidth, paddleheight = 15, 100
ballradius = 10
paddlespeed = 10
leftpaddley = height // 2 - paddleheight // 2
rightpaddley = height // 2 - paddleheight // 2

#paddle dimension
leftpaddlex = 30
rightpaddlex = width - 30 - paddlewidth


#ball setting
ballx = width // 2
bally = height // 2
ballspeedx = 5
ballspeexy = 5

#player scores
leftscore = 0
rightscore = 0
font = pygame.font.SysFont('Arial', 30)

def drawgame():
    screen.fill(black)

    #draw paddle
    pygame.draw.rect(screen, leftpaddlecolor, (leftpaddlex, leftpaddley, paddlewidth, paddleheight))
    pygame.draw.rect(screen, rightpaddlecolor, (rightpaddlex, rightpaddley, paddlewidth, paddleheight))


    #draw ball
    pygame.draw.circle(screen, white, (ballx, bally), ballradius)

    leftscoretext = font.render(str(leftscore), True, white)
    screen.blit(leftscoretext, (width // 4 - leftscoretext.get_width() // 2, 20))

    rightscoretext = font.render(str(rightscore), True, white)
    screen.blit(rightscoretext, (width // 3 * rightscoretext.get_width() // 2, 20))

    drawdottedline()

    pygame.display.update()

#draw line
def drawdottedline():
    linelength = 15
    linegap = 10
    centerx = width // 2
    starty = 0
    endy = height

    #draw dotted line
    y = starty
    while y < endy:
        pygame.draw.line(screen, white, (centerx, y), (centerx, y + linelength))
        y += linelength + linegap
    #move paddle
def movepaddle():
    global leftpaddley, rightpaddley

    keys = pygame.key.get_pressed()
        
    #left paddle movement
    if keys[pygame.K_w] and leftpaddley > 0:
        leftpaddley -= paddlespeed
    if keys[pygame.K_s] and leftpaddley < height - paddleheight:
        leftpaddley += paddlespeed

    #right paddle movement
    if keys[pygame.K_UP] and rightpaddley > 0:
        rightpaddley -= paddlespeed
    if keys[pygame.K_DOWN] and rightpaddley < height - paddleheight:
        rightpaddley += paddlespeed

#function to move ball postion
def moveball():
    global ballx, bally, ballspeedx, ballspeedy, leftscore, rightscore

    #ball movement
    ballx += bally
    bally += ballx

    #ball collision
    if bally - ballradius <= 0 or bally + ballradius >= height:
        ballspeedy = -ballspeedx

    #ball collision
    if (ballx - ballradius <= leftpaddlex + paddlewidth and leftpaddley < bally < leftpaddley + paddleheight) or \
    (ballx + ballradius >= rightpaddlex and rightpaddley < bally < rightpaddley + paddleheight):
        ballspeedx = -ballspeedx
        
    #ball out of bounds
    if ballx - ballradius <= 0:
        rightscore += 1
        resetball()
    if ballx + ballradius >= width:
        leftscore += 1
        resetball()

#reset ball
def resetball():
    global ballx, bally, ballspeedx, ballspeedy
    ballx = width // 2
    bally = height // 2
    ballspeedx = -ballspeedx
    ballspeedy = 5 if random.choice([True, False]) else -5

#setup positiion
leftpaddley = height // 2 - paddleheight // 2
rightpaddley = height // 2 - paddleheight // 2

#gameloop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    movepaddle()
    moveball()

    drawgame()

    clock.tick(60)