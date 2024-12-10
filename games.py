import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Create the screen
width = 800
height = 600
screen_color = (0, 0, 0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game in Python")

# Player variables
player_width = 100
player_height = 20
playerx = (width - player_width) // 2
playery = (height - player_height - 30) # player is a little above the bottom edge
player_color = (0, 255, 0)
player_speed = 7

# Ball variables (yellow ball)
ball_radius = 15
ball_y = -ball_radius
ball_x = random.randint(ball_radius, width - ball_radius)
ball_speed = 5
ball_color = (245, 233, 66) # yellow

# Red Ball variables (for Game Over)
red_ball_radius = 15
red_ball_y = -red_ball_radius
red_ball_x = random.randint(red_ball_radius, width - red_ball_radius)
red_ball_speed = 4
red_ball_color = (255, 0, 0) # red

# Score variables
score = 0
text_color = (255, 255, 255)
font = pygame.font.SysFont("Arial", 20)
gameoverfont = pygame.font.SysFont("Arial", 100)

# Clock variable
clock = pygame.time.Clock()

# Game Over state
game_over = False
game_over_time = 0

# Main game loop
running = True
while running:
    # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if game_over:
            # Display "Game Over" and wait for 2 seconds
            game_over_text = gameoverfont.render("Game Over", True, (255, 0, 0))
            screen.fill(screen_color)
            screen.blit(game_over_text, ((width - game_over_text.get_width()) // 2, height // 2 - 50))
            pygame.display.update()
            time.sleep(2)
            running = False
            break
    # Moving the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and playerx > 0:
            playerx -= player_speed
        if keys[pygame.K_RIGHT] and playerx < (width - player_width):
            playerx += player_speed
    # Making the ball fall from the top (yellow ball)
        ball_y += ball_speed
    # Making the red ball fall from the top
        red_ball_y += red_ball_speed
    # Check collision with the bottom edge for the yellow ball
        if ball_y > height:
            ball_y = -ball_radius
            ball_x = random.randint(ball_radius, width - ball_radius)
    # Check collision with the bottom edge for the red ball
        if red_ball_y > height:
            red_ball_y = -red_ball_radius
            red_ball_x = random.randint(red_ball_radius, width - red_ball_radius)
    # Checking collision with the player (yellow ball)
        if (playerx < ball_x < playerx + player_width) and (playery < ball_y + ball_radius < playery + player_height):
            score += 10
            ball_y = -ball_radius
            ball_x = random.randint(ball_radius, width - ball_radius)
    # Checking collision with the player (red ball)
        if (playerx < red_ball_x < playerx + player_width) and (playery < red_ball_y + red_ball_radius < playery + player_height):
            game_over = True
            game_over_time = pygame.time.get_ticks()
    # Fill the screen with the background color
        screen.fill(screen_color)
    # Draw player, balls, and the score
        pygame.draw.rect(screen, player_color, (playerx, playery, player_width, player_height))
        pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
        pygame.draw.circle(screen, red_ball_color, (red_ball_x, red_ball_y), red_ball_radius)
    # Display the score
        score_text = font.render(f"Score: {score}", True, text_color)
        screen.blit(score_text, (10, 10))
    # Update the screen
        pygame.display.update()
        # Set the frames per second
        clock.tick(50)
    # Quit Pygame
pygame.quit()