import pygame
from sys import exit
from pathlib import Path

# game variables
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512

PLAYER_X = WINDOW_WIDTH / 2
PLAYER_Y = WINDOW_HEIGHT / 2
PLAYER_WIDTH = 42
PLAYER_HEIGHT = 48

# images
image_dir = Path("images/")

background_image = pygame.image.load(str(image_dir) + "/background.png")
player_image_right = pygame.image.load(str(image_dir) + "/megaman-right.png")
player_image_right = pygame.transform.scale(
    player_image_right, (PLAYER_WIDTH, PLAYER_HEIGHT)
)


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Smith Intro Game")  # title of window
pygame.display.set_icon(player_image_right)
clock = pygame.time.Clock()  # used for frame rate


class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_image_right


player = Player()


def draw():
    window.fill((20, 18, 167))  # rgb tuple fills background
    window.blit(background_image, (0, 80))  # order matters!
    window.blit(player.image, player)


while True:  # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # user clicks the X button in window
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
    clock.tick(60)  # 60 frames per second (fps)
