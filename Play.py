import pygame
import sys
from configs import configs
from modules.Game import Game

pygame.init()
screen = pygame.display.set_mode((configs.WIN_WIDTH, configs.WIN_HEIGHT))
pygame.display.set_caption("Ding Snake Game")

game = Game(screen)

while True:
    event = None
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 0
            elif event.key == pygame.K_RIGHT:
                direction = 1
            elif event.key == pygame.K_DOWN:
                direction = 2
            elif event.key == pygame.K_LEFT:
                direction = 3
            else:
                continue

            observe, reward, len, lose = game.moveByAbsoluteDirection(direction)
            if lose:
                sys.exit()

    if event is None:
        observe, reward, len, lose = game.moveByRelativeDirection(0)
        if lose:
            sys.exit()

    pygame.display.update()
    pygame.time.Clock().tick(configs.GAME_FPS)
