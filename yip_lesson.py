import pygame
from sys import exit
from pathlib import Path
import os

# game variables
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512

PLAYER_X = WINDOW_WIDTH / 2
PLAYER_Y = WINDOW_HEIGHT / 2
PLAYER_WIDTH = 42
PLAYER_HEIGHT = 48
PLAYER_JUMP_WIDTH = 52
PLAYER_JUMP_HEIGHT = 60
PLAYER_DISTANCE = 5


PLAYER_VELOCITY_Y = -10
GRAVITY = 0.5
FLOOR_Y = WINDOW_HEIGHT * 3/4

def load_image(image_name,scale=None):
    # images
    image_dir = Path("images")
    image = pygame.image.load(str(image_dir)+"/"+image_name)
    if scale is not None:
        image = pygame.transform.scale(image,scale)
    return image

background_image = load_image("background.png")
player_image_right = load_image("megaman-right.png",(PLAYER_WIDTH, PLAYER_HEIGHT))
player_image_left = load_image("megaman-left.png",(PLAYER_WIDTH, PLAYER_HEIGHT))
player_image_jump_right = load_image("megaman-right-jump.png",(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player_image_jump_left = load_image("megaman-left-jump.png",(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))



pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Smith Intro Game")  # title of window
pygame.display.set_icon(player_image_right)
clock = pygame.time.Clock()  # used for frame rate


class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_image_right
        self.velocity_y = 0
        self.jumping = False # prevents double jumping
        self.direction = "right"
    
    def update_image(self):
        if self.jumping:
            self.width = PLAYER_JUMP_WIDTH
            self.height = PLAYER_JUMP_HEIGHT
            if self.direction == "right":
                self.image = player_image_jump_right
            elif self.direction == "left":
                self.image = player_image_jump_left

        else:
            if self.direction == "right":
                self.image = player_image_right
            elif self.direction == "left":
                self.image = player_image_left

player = Player()

def move():
    player.velocity_y += GRAVITY
    player.y += player.velocity_y

    if player.y + player.height > FLOOR_Y:
        player.y = FLOOR_Y-player.height
        player.jumping = False


def draw():
    window.fill((20, 18, 167))  # rgb tuple fills background, transparent otherwise if I remove this
    window.blit(background_image, (0, 80))  # order matters!
    player.update_image()
    window.blit(player.image, player)


while True:  # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # user clicks the X button in window
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not player.jumping:
        player.velocity_y = PLAYER_VELOCITY_Y
        player.jumping = True
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        player.x = max(player.x-PLAYER_DISTANCE,0)
        player.direction = "left"
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x = min(player.x + PLAYER_DISTANCE,WINDOW_WIDTH-player.width)
        player.direction = "right"

    move()
    draw()
    pygame.display.update()
    clock.tick(60)  # 60 frames per second (fps)
