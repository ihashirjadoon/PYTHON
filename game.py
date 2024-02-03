import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Characters
player = pygame.Rect(50, HEIGHT // 2, 50, 50)
enemy = pygame.Rect(WIDTH - 100, HEIGHT // 2, 50, 50)

# Character speeds
player_speed = 5
enemy_speed = 3

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Combat Game")

def draw_characters():
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, RED, enemy)

def main():
    global player, enemy

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

        enemy.x -= enemy_speed

        # Collision check
        if player.colliderect(enemy):
            print("Collision! Game Over.")
            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        draw_characters()w
        pygame.display.flip()

        clock.tick(30)

if __name__ == "__main__":
    main()
