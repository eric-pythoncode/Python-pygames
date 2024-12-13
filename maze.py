import pygame

pygame.init()

width = 600
height = 400
screen = pygame.display.set_mode((width , height))
pygame.display.set_caption("Maze Game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

playersize = 20
playerx, playery = 50, 50
playerspeed = 5

goalsize = 30
goalx, goaly = 550, 350

#walls (x, y, width, height)
walls = [
    (100, 0, 20, 300),
    (200, 100, 20, 300),
    (300, 0, 20, 300),
    (400, 100, 20, 300),
    (500, 0, 20, 300)
]

font = pygame.font.SysFont("Arial", 50)

#game loop
clock = pygame.time.Clock()
running  = True
won = False
wintime = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #movent
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and playery > 0:
        playery -= playerspeed
    if keys[pygame.K_DOWN] and playery <= height - playersize:
        playery += playerspeed
    if keys[pygame.K_RIGHT] and playerx <= width - playersize:
        playerx += playerspeed
    if keys[pygame.K_LEFT] and playery >= 0:
        playerx -= playerspeed
    
    #collision with wall
    playerrect = pygame.Rect(playerx, playery, playersize, playersize)
    for wall in walls:
        wallrect = pygame.Rect(wall)
        if playerrect.colliderect(wallrect):
            if keys[pygame.K_UP]:
                playery += playerspeed
            if keys[pygame.K_DOWN]:
                playery -= playerspeed
            if keys[pygame.K_RIGHT]:
                playerx -= playerspeed
            if keys[pygame.K_LEFT]:
                playerx += playerspeed
    
    
    #check if player reaches goal
    goalrect = pygame.Rect(goalx, goaly, goalsize, goalsize)
    if playerrect.colliderect(goalrect) and not won:
        won = True
        wintime = pygame.time.get_ticks() #record time
    
    #draw
    screen.fill(white)
    pygame.draw.rect(screen, red, playerrect)
    pygame.draw.rect(screen, green, goalrect)
    for wall in walls:
        pygame.draw.rect(screen, blue, wall)
    
    if won:
        wintext = font.render("You win!", True, (0, 0, 0))
        screen.blit(wintext, (width // 2 - wintext.get_width() // 2, height // 2))

        if pygame.time.get_ticks() - wintime >= 2000:
            running = False
        
    pygame.display.update()
    clock.tick(40)

pygame.quit()