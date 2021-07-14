import pygame, sys, random, time
#import sys
#import random

WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)

player_size = [50, 50]
player_pos = [WIDTH//2, HEIGHT-2*player_size[1]]
player_speed = player_size[0] //2

ENEMYSPEED = 4
enemy_size = [50, 50]
enemy_pos_speed = [random.randint(0, WIDTH-enemy_size[0]), 1, ENEMYSPEED]
enemy_list = [enemy_pos_speed]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
score_font = pygame.font.SysFont("monospace", 25)
score = 0
game_over = False

def generate_enemy(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.005:
        enemy_list.append([random.randint(0, WIDTH-enemy_size[0]), -enemy_pos_speed[1], ENEMYSPEED+random.randint(-2,2)])
    elif len(enemy_list) >= 10 and delay < 0.003:
        enemy_list.append([random.randint(0, WIDTH-enemy_size[0]), -enemy_pos_speed[1], ENEMYSPEED+random.randint(-2,2)])

def detect_collision(player_pos, enemy_pos_speed):
    if player_pos[1] + player_size[1] >= enemy_pos_speed[1] and player_pos[1] <= enemy_pos_speed[1] + enemy_size[1]:
        if player_pos[0] + player_size[0] >= enemy_pos_speed[0] and player_pos[0] <= enemy_pos_speed[0] + enemy_size[0]:
            return True
    else:
        return False

def enemy_speed_pos_update(enemy_list, score):
    #set enemy speed and pos
    for enemy_pos_speed in enemy_list:
        if enemy_pos_speed[1] < HEIGHT + 10:
            enemy_pos_speed[1] += enemy_pos_speed[2]
        else:
            enemy_pos_speed[1] = -enemy_size[1]
            enemy_pos_speed[0] = random.randint(0, WIDTH-enemy_size[0])
            score += 1
    return enemy_list, score



def player_movement(player_pos, player_speed):
    pygame.key.set_repeat(200,50)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if player_pos[0] > 0:
                player_pos[0] -= player_speed
        elif event.key == pygame.K_RIGHT:
            if player_pos[0] < (WIDTH-player_size[0]):
                player_pos[0] += player_speed
    return player_pos, player_speed

def score_board(score, enemy_list):
    #text on screen
    text1 = "Score: " + str(score)
    text2 = "Enemy: " + str(len(enemy_list))
    score_label = score_font.render(text1, 1, YELLOW)
    enemy_label = score_font.render(text2, 1, YELLOW)
    screen.blit(score_label, (WIDTH-150, 5))
    screen.blit(enemy_label, (WIDTH-150, 45))

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)
    player_pos, player_speed = player_movement(player_pos, player_speed)
    enemy_list, score = enemy_speed_pos_update(enemy_list, score)

    for enemy_pos_speed in enemy_list:
        if detect_collision(player_pos, enemy_pos_speed):
            time.sleep(5)
            sys.exit()

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size[0], player_size[1]), 3) #3 is line width use 0 for filled
    generate_enemy(enemy_list)
    for enemy_pos_speed in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos_speed[0], enemy_pos_speed[1], enemy_size[0], enemy_size[1]), 3)

    score_board(score, enemy_list)

    clock.tick(30)
    pygame.display.update()
