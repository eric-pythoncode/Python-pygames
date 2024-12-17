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
yellow = (255, 255, 0)

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

#coins
coins = [
    (150, 150, 15, 15),
    (250, 50, 15, 15),
    (250, 250, 15, 15),
    (450, 150, 15, 15),
]

#hazards
obstacles = [
    [180, 200, 20, 20, 3, 2],
    [380, 100, 2, 20, 2, -3]
]

score = 0



font = pygame.font.SysFont("Arial", 50)

#game loop
clock = pygame.time.Clock()
running  = True
won = False
messagetime = 0
gameover = False

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

    collectedcoins = []
    for coin in coins:
        coinrect = pygame.Rect(coin)
        if playerrect.colliderect(coinrect):
            score += 10
            collectedcoins.append(coin)
    coins = [coin for coin in coins if coin not in collectedcoins]

    for obstacle in obstacles:
        obstaclerect = pygame.Rect(obstacle[0], obstacle[1], obstacle[2], obstacle[3])
        if playerrect.colliderect(obstaclerect):
            gameover = True
            messagetime = pygame.time.get_ticks()
            break

    
    
    #check if player reaches goal
    goalrect = pygame.Rect(goalx, goaly, goalsize, goalsize)
    if playerrect.colliderect(goalrect) and not won:
        won = True
        messagetimetime = pygame.time.get_ticks() #record time
        break

    
    #draw
    screen.fill(white)
    pygame.draw.rect(screen, red, playerrect)
    pygame.draw.rect(screen, green, goalrect)
    for wall in walls:
        pygame.draw.rect(screen, blue, wall)
    for coin in coins:
        pygame.draw.rect(screen, yellow, coin)
    for obstacle in obstacles:
        pygame.draw.rect(screen, red, (obstacle[0], obstacle[1], obstacle[2], obstacle[3]))
    
    if won:
        wintext = font.render(f"You win! Score: {score}", True, (0, 0, 0))
        screen.blit(wintext, (width // 2 - wintext.get_width() // 2, height // 2))

        if pygame.time.get_ticks() - messagetime >= 2000:
            running = False

    if gameover:
        gameovertext = font.render("Game over!", True, (0, 0, 0))
        screen.blit(wintext, (width // 2 - wintext.get_width() // 2, height // 2))

        if pygame.time.get_ticks() - messagetime >= 2000:
            running = False
        
    pygame.display.update()
    clock.tick(40)

pygame.quit()
