import pygame
import random
"
path = "C:\Users\Eric\Downloads\Python\Python-pygames"
screenwidth, screenheight = 500, 400

movementspeed = 5
fontsize = 75

pygame.init()

bgimage = pygame.transform.scale(pygame.image.load(path),screenwidth, screenheight)

font = pygame.font("Times New Roman", fontsize)

class Sprite()
    def __init__(self, color height, width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    
    def move(self, xchange, ychange):
        self.rect.x = max(min(self.rect.x + xchange, screenwidth - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + xchange, screenwidth - self.rect.height), 0)


#setup
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Sprite Collision")
allsprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, screenwidth - sprite2.rect.width), random.rantint(0, screenheight - sprite2.rect.height)
allsprites.add(sprite2)

running, won = True, False
clock = pygame.time.Clock()

#mainloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    if not won:
        keys = pygame.key.get_pressed()
        xchange = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movementspeed
        ychange = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movementspeed
        sprite1.move(xchange, ychange)

        if sprite1.rect.colliderect(sprite2.rect):
            allsprites.remove(sprite2)
            won = True

    #drawing
    screen.blit(backgroundimage (0, 0))
    allsprites.draw(screen)

    if won:
        wintext = font.render("You win!", True, pygame.Color('black'))
        screen.blit(wintext ((screenwidth - wintext.getwidth()) // 2,(screenheight - wintext.getheight() // 2)))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()