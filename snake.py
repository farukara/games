import pygame
from typing import List


class Snake():
    def __init__(self, head_position: List= [400,300], body_positions=[[360,300],[320,300],[280,300]]):
        self.head_position = head_position
        self.body_positions = body_positions
    
def snake_movement(head_position, key, movement_direction):
    if movement_direction == "L":
        if key == 'L':
            head_position[0] -= snake_size[0]
        elif key == 'U':
            head_position[1] -= snake_size[0]
            movement_direction = 'U'
        elif key == 'D':
            head_position[1] += snake_size[0]
            movement_direction = 'D'
        elif key == 'R': #no effect
            head_position[0] -= snake_size[0]
    elif movement_direction == "R":
        if key == 'R':
            head_position[0] += snake_size[0]
        elif key == 'U':
            head_position[1] -= snake_size[0]
            movement_direction = 'U'
        elif key == 'D':
            head_position[1] += snake_size[0]
            movement_direction = 'D'
        elif key == 'L': #no effect
            head_position[0] += snake_size[0]
    elif movement_direction == "U":
        if key == 'L':
            head_position[0] -= snake_size[0]
            movement_direction = 'L'
        elif key == 'U':
            head_position[1] -= snake_size[0]
        elif key == 'R':
            head_position[0] += snake_size[0]
            movement_direction = 'R'
        elif key == 'D': #no effect
            head_position[1] -= snake_size[0]
    elif movement_direction == "D":
        if key == 'L':
            head_position[0] -= snake_size[0]
            movement_direction = 'L'
        elif key == 'R':
            head_position[0] += snake_size[0]
            movement_direction = 'R'
        elif key == 'D':
            head_position[1] += snake_size[0]
        elif key == 'U': #no effect
            head_position[1] += snake_size[0]
        
    return head_position, movement_direction


def main():
    global WIDTH, HEIGHT, BLACK, BLUE, snake_size, snake_speed, key, movement_direction, event
    WIDTH = 800
    HEIGHT = 600
    BLACK = (0,0,0)
    BLUE = (0,0,200)
    snake_size = [40, 40]
    #snake_speed = 5
    key = "R"
    movement_direction = 'R'

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake()
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key = 'L'
                elif event.key == pygame.K_RIGHT:
                    key = 'R'
                elif event.key == pygame.K_UP:
                    key = 'U'
                elif event.key == pygame.K_DOWN:
                    key = 'D'
        screen.fill(BLACK)
        snake.body_positions.insert(0, [snake.head_position[0], snake.head_position[1]])
        snake.body_positions.pop()
        snake.head_position, movement_direction = snake_movement(snake.head_position, key,  movement_direction)

        pygame.draw.rect(screen, BLUE, (snake.head_position[0], snake.head_position[1], snake_size[0], snake_size[1]), 3)
        for single_body in snake.body_positions:
            pygame.draw.rect(screen, BLUE, (single_body[0], single_body[1], snake_size[0], snake_size[1]), 3)
            

        clock.tick(30)
        pygame.time.delay(300)
        pygame.display.update()

if __name__ == "__main__":
    main()
