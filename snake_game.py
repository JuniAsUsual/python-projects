import pygame
import time
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
speed = 15

food_pos = [random.randrange(1, (WIDTH//10)) * 10,
             random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

score = 0

font = pygame.font.SysFont("Arial", 25)

def show_score():
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    win.blit(score_text, [10, 10])

def game_over():
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to
    if direction == 'UP': snake_pos[1] -= 10
    if direction == 'DOWN': snake_pos[1] += 10
    if direction == 'LEFT': snake_pos[0] -= 10
    if direction == 'RIGHT': snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10,
                    random.randrange(1, (HEIGHT//10)) * 10]
    food_spawn = True

    win.fill((255, 255, 255))
    for segment in snake_body:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    show_score()
    pygame.display.update()

    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10 or snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    clock.tick(speed)
