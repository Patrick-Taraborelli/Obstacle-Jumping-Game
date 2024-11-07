import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Screen settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jumping Obstacles Game")

# FPS (frames per second)
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT - 70)
        self.velocity_y = 0
        self.jump_strength = -15
        self.gravity = 1

    def update(self):
        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Prevent player from falling through the ground
        if self.rect.bottom > SCREEN_HEIGHT - 10:
            self.rect.bottom = SCREEN_HEIGHT - 10
            self.velocity_y = 0

    def jump(self):
        if self.rect.bottom == SCREEN_HEIGHT - 10:
            self.velocity_y = self.jump_strength

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - 70
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = SCREEN_HEIGHT - 70

# Create sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create obstacles
for i in range(5):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Main game loop
running = True
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Update all sprites
    all_sprites.update()

    # Check for collision with obstacles
    if pygame.sprite.spritecollide(player, obstacles, False):
        print("You collided with an obstacle! Game Over.")
        running = False

    # Fill the screen with background color
    screen.fill(BLACK)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Control FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
