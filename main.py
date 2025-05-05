import pygame
from sys import exit

def main():
    pygame.init()
    WINDOW_WIDTH = 512
    WINDOW_HEIGHT = 512
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Smith Intro Game") # title of window
    clock = pygame.time.Clock() # used for frame rate
    
    while True: # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # user clicks the X button in window
                pygame.quit()
                exit()
                
        pygame.display.update()
        clock.tick(60) # 60 frames per second (fps)

if __name__ == "__main__":
    main()