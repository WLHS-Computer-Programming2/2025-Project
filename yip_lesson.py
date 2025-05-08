import pygame
from sys import exit


pygame.init()
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Smith Intro Game") # title of window
clock = pygame.time.Clock() # used for frame rate

# left (x), top (y), width, height
player = pygame.Rect(150,150,50,50)

def draw():
    window.fill((20,18,167)) # rgb tuple fills background
    pygame.draw.rect(window,(2,239,238),player)

while True: # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # user clicks the X button in window
            pygame.quit()
            exit()
    
        # if event.type == pygame.KEYDOWN: # if key is pressed down and released
        #     if event.key in (pygame.K_UP, pygame.K_w):
        #         player.y -= 10
        #     if event.key in (pygame.K_DOWN, pygame.K_s):
        #         player.y += 10
        #     if event.key in (pygame.K_LEFT, pygame.K_a):
        #         player.x -= 10
        #     if event.key in (pygame.K_RIGHT, pygame.K_d):
        #         player.x += 10
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += 5
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 5
        
        
    draw()
    pygame.display.update()
    clock.tick(60) # 60 frames per second (fps)



