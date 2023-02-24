import pygame, sys
from constants import *
from classes import *

pygame.init()

pygame.display.set_caption('Snakeman')
screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))
clock = pygame.time.Clock()

#Set the timer for the screen update to slow down the movement of the snake
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 100)

main = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main.update()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main.snake.direction != v2(0,1):
                main.snake.direction = v2(0,-1)
            if event.key == pygame.K_DOWN and main.snake.direction != v2(0,-1):
                main.snake.direction = v2(0,1)
            if event.key == pygame.K_LEFT and main.snake.direction != v2(1,0):
                main.snake.direction = v2(-1,0)
            if event.key == pygame.K_RIGHT and main.snake.direction != v2(-1,0):
                main.snake.direction = v2(1,0)

    screen.fill((100,100,100))
    main.draw_elements(screen)
    pygame.display.update()
    clock.tick(FPS)