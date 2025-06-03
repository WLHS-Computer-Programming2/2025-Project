import pygame
from sys import exit
from pathlib import Path
import os

# game variables
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512

BIRD_X = WINDOW_WIDTH / 2
BIRD_Y = WINDOW_HEIGHT / 2
BIRD_WIDTH = 128
BIRD_HEIGHT = 128
BIRD_JUMP_WIDTH = 52
BIRD_JUMP_HEIGHT = 60
BIRD_DISTANCE = 5


BIRD_VELOCITY_Y = -10
GRAVITY = 0.5
FLOOR_Y = WINDOW_HEIGHT * 3/4

def load_image(image_path,scale=None):
    # images
    image = pygame.image.load(image_path)
    if scale is not None:
        image = pygame.transform.scale(image,scale)
    return image

# images

background_image = load_image(Path(r"assets\forest_v1\background\fores_background full.png"),(WINDOW_WIDTH,WINDOW_HEIGHT))
default_bird = load_image(Path(r"assets\bird_1_red\bird_1_red_15.png"),(64,64))
bird_ground_right = load_image(Path(r"assets\bird_1_red\bird_1_red_22.png"),(64,64))

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bird Adventures")  # title of window
pygame.display.set_icon(default_bird)
clock = pygame.time.Clock()  # used for frame rate

class Bird(pygame.Rect):
    def __init__(self):
         pygame.Rect.__init__(self, BIRD_X, BIRD_Y, BIRD_WIDTH, BIRD_HEIGHT)
         self.image = default_bird
         self.velocity_y = 0
         self.jumping = False
         self.direction = "right"

    def update_image(self):
        if self.direction == "right":
            self.image = bird_ground_right
        elif self.direction == "left":
            self.image = default_bird

bird = Bird()

def move():
    bird.velocity_y += GRAVITY
    bird.y += bird.velocity_y

    if bird.y + bird.height > FLOOR_Y:
        bird.y = FLOOR_Y-bird.height
        bird.jumping = False

def draw():
    window.fill((20, 18, 167))  # rgb tuple fills background, transparent otherwise if I remove this
    window.blit(background_image, (0, 0))  # order matters!
    bird.update_image()
    window.blit(bird.image, bird)

while True:  # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # user clicks the X button in window
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not bird.jumping:
        bird.velocity_y = BIRD_VELOCITY_Y
        bird.jumping = True
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        bird.x = max(bird.x-BIRD_DISTANCE,0)
        bird.direction = "left"
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        bird.x = min(bird.x + BIRD_DISTANCE,WINDOW_WIDTH-bird.width)
        bird.direction = "right"


    draw()
    move()
    pygame.display.update()
    clock.tick(60)  # 60 f