import pygame

# Initialize Pygame

pygame.init()

# Create the screen

screen = pygame.display.set_mode((500 , 500))

pygame.display.set_caption("Game in Python")

#main game loop

running = True

while running:

#handling events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

pygame.quit()