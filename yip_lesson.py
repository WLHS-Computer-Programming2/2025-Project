import pygame
from sys import exit


pygame.init()
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Smith Intro Game") # title of window
clock = pygame.time.Clock() # used for frame rate
player = pygame.Rect(150,150,50,50)

def draw():
    window.fill((20,18,167)) # rgb tuple fills background
    
    pygame.draw.rect(window,(2,239,238),player)

while True: # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # user clicks the X button in window
            pygame.quit()
            exit()
    
    draw()
    pygame.display.update()
    clock.tick(60) # 60 frames per second (fps)



