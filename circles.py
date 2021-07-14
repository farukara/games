import pygame, sys, math, random, time

WIDTH = 1000
HEIGHT = 700
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() 
player_pos = [100, 100]
player_radius = 50
player_speed = 5
enemy_list = [[200,100,40]] #x,y,radius
osmosis_speed = 1
score = 0
score_font = pygame.font.SysFont("monospace", 25)

def player_movement(player_pos, player_speed):
    pygame.key.set_repeat(200,50)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if player_pos[0] > player_radius:
                player_pos[0] -= player_speed
        elif event.key == pygame.K_RIGHT:
            if player_pos[0] < (WIDTH - player_radius):
                player_pos[0] += player_speed
        elif event.key == pygame.K_UP:
            if player_pos[1] > player_radius:
                player_pos[1] -= player_speed
        elif event.key == pygame.K_DOWN:
            if player_pos[1] < HEIGHT - player_radius:
                player_pos[1] += player_speed
    return player_pos

def touch_detection(player_pos, enemy):
    distance = math.sqrt((player_pos[0] - enemy[0])**2 + (player_pos[1] - enemy[1])**2)
    if distance < player_radius + enemy[2]:
        return True

def osmosis(player_pos, player_radius, enemy, score):
    if player_radius > enemy[2] and enemy[2] > 0:
        player_radius += osmosis_speed
        enemy[2] -= osmosis_speed
        score += 1
    elif player_radius <= enemy[2] and player_radius > 0:
        player_radius -= osmosis_speed
        enemy[2] += osmosis_speed
    #moving player away form target during osmosis
    if player_pos[0] < enemy[0]:
        player_pos[0] -= osmosis_speed*2
    else:
        player_pos[0] += osmosis_speed*2
    if player_pos[1] < enemy[1]:
        player_pos[1] -= osmosis_speed*2
    else:
        player_pos[1] += osmosis_speed*2
    
    return player_pos, player_radius, enemy[2], score

def enemy_generation(enemy_list):
    delay = random.random()
    if delay < 0.1:
        candidate_radius = random.randint(10,150)
        candidate = [random.randint(candidate_radius, WIDTH-candidate_radius), random.randint(candidate_radius, HEIGHT-candidate_radius), candidate_radius]
        empty_emerge_location = True
        for enemy in enemy_list:
            if touch_detection([candidate[0], candidate[1]], enemy) or touch_detection(player_pos, candidate):
                empty_emerge_location = False
        if empty_emerge_location:
            enemy_list.append(candidate)
    return enemy_list

def score_board(score, enemy_list):
    #text on screen
    text1 = "Score: " + str(score)
    text2 = "Number of Blue: " + str(len(enemy_list))
    score_label = score_font.render(text1, 1, YELLOW)
    enemy_label = score_font.render(text2, 1, YELLOW)
    screen.blit(score_label, (WIDTH-250, 5))
    screen.blit(enemy_label, (WIDTH-300, HEIGHT-35))

gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    player_pos = player_movement(player_pos, player_speed)
    enemy_list = enemy_generation(enemy_list)
    new_enemylist = []
    for enemy in enemy_list:
        if touch_detection(player_pos, enemy):
            player_pos, player_radius, enemy[2], score = osmosis(player_pos, player_radius, enemy, score)
        if enemy[2] > osmosis_speed:
            new_enemylist.append(enemy)
    enemy_list = new_enemylist

    if player_radius > HEIGHT //10:
        player_radius -= 1
        for enemy in enemy_list:
            enemy[2] -= 1

    screen.fill(BLACK)
    score_board(score, enemy_list)
    pygame.draw.circle(screen, RED, player_pos, player_radius, width=4)
    for enemy in enemy_list:
        pygame.draw.circle(screen, BLUE, (enemy[0], enemy[1]), enemy[2])

    if player_radius == osmosis_speed:
        time.sleep(3)
        sys.exit()
    clock.tick(30)
    pygame.display.update()
