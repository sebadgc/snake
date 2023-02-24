import pygame,random
from constants import *
from pygame.math import Vector2 as v2

class FRUIT:
    #Initialize the fruit on a random position
    def __init__(self):
        self.randomize_position()

    def randomize_position(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = v2(self.x, self.y)

    def draw_fruit(self, screen):
        x_pos = self.pos.x*CELL_SIZE
        y_pos = self.pos.y*CELL_SIZE
        fruit_rect = pygame.Rect(x_pos, y_pos , CELL_SIZE, CELL_SIZE)
        fruit_sprite = pygame.image.load(f'sprites/fruits/{1}.png').convert_alpha()
        screen.blit(fruit_sprite, fruit_rect)


class SNAKE:
    def __init__(self):
        self.body = [v2(15,15), v2(16,15), v2(17,15)]
        self.direction = v2(1,0)   
        self.grow = False

    def draw_snake(self, screen):
        for block in self.body:
            x_pos = block.x*CELL_SIZE
            y_pos = block.y*CELL_SIZE
            block_rect = pygame.Rect(x_pos, y_pos , CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (50,220,50), block_rect)

    def move_snake(self):
        if self.grow:
            body_old = self.body[:]
            body_old.insert(0,body_old[0] + self.direction)
            self.body = body_old[:]
            self.grow = False
        else:
            body_old = self.body[:-1]
            body_old.insert(0,body_old[0] + self.direction)
            self.body = body_old[:]


class MAIN:
    #Use a main class to englobe both the snake and the fruits
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self, screen):
        self.fruit.draw_fruit(screen)
        self.snake.draw_snake(screen)
    
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize_position()
            self.snake.grow = True

    def check_fail(self):
        #Check if the snake is out of bounds
        if (not 0 <= self.snake.body[0].x <= CELL_SIZE or not 
             0 <= self.snake.body[0].y <= CELL_SIZE):
            self.game_over()
      
        #Check if the snake hit itself
        if self.snake.body[0] in self.snake.body[1:]:
            self.game_over()

    def game_over(self):
        print('Game Over')
        