import pygame

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
BLUE = (0,0,200)
snake_pos = [400,300]
snake_size = [20, 20]
snake_speed = 5
snake_len = [[100,200]]
key = "R"
movement_direction = 'R'

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def snake_movement(snake_pos, snake_speed, key, movement_direction):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            key = 'L'
        if event.key == pygame.K_RIGHT:
            key = 'R'
        if event.key == pygame.K_UP:
            key = 'U'
        if event.key == pygame.K_DOWN:
            key = 'D'
    if movement_direction == "L":
        if key == 'L':
            snake_pos[0] -= snake_speed
            movement_direction = 'L'
        if key == 'U':
            snake_pos[1] -= snake_speed
            movement_direction = 'U'
        if key == 'D':
            snake_pos[1] += snake_speed
            movement_direction = 'D'
    if movement_direction == "R":
        if key == 'R':
            snake_pos[0] += snake_speed
            movement_direction = 'R'
        if key == 'U':
            snake_pos[1] -= snake_speed
            movement_direction = 'U'
        if key == 'D':
            snake_pos[1] += snake_speed
            movement_direction = 'D'
    if movement_direction == "U":
        if key == 'L':
            snake_pos[0] -= snake_speed
            movement_direction = 'L'
        if key == 'U':
            snake_pos[1] -= snake_speed
            movement_direction = 'U'
        if key == 'R':
            snake_pos[0] += snake_speed
            movement_direction = 'R'
    if movement_direction == "D":
        if key == 'L':
            snake_pos[0] -= snake_speed
            movement_direction = 'L'
        if key == 'R':
            snake_pos[0] += snake_speed
            movement_direction = 'R'
        if key == 'D':
            snake_pos[1] += snake_speed
            movement_direction = 'D'
        
    return snake_pos, key, movement_direction

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.fill(BLACK)
    snake_pos, key, movement_direction = snake_movement(snake_pos, snake_speed, key, movement_direction)

    pygame.draw.rect(screen, BLUE, (snake_pos[0], snake_pos[1], snake_size[0], snake_size[1]), 3)
    for i in snake_len:
        pygame.draw.rect(screen, BLUE, (i[0], i[1], snake_size[0], snake_size
            [1]), 3)
    snake_len.append([snake_pos[0], snake_pos[1]])
    snake_len.append([snake_pos[0], snake_pos[1]])
    snake_len.pop(0)
    clock.tick(30)
    pygame.display.update()

    
