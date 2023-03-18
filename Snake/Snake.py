import pygame
import sys
import time
import random


def game_over(score):  # функция выхода из игры и отрисовки надписи

    f1 = pygame.font.SysFont('times new roman', 80)
    text1 = f1.render('Game over', True, red)

    f2 = pygame.font.SysFont('times new roman', 60)
    text2 = f2.render('Score: ' + str(score), False,green)

    game_window.blit(text1, (frame_size_x / 2 -180, 125))
    game_window.blit(text2, (frame_size_x / 2 - 90, 220))
    pygame.display.update()

    time.sleep(3)
    pygame.quit()  #
    sys.exit()  #



def food_poss(frame_size_x, frame_size_y, fence): #[[110, 84, 310, 84], [254, 252, 254, 398], [0, 424, 300, 424]]
    while True:
        x = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10] #[110, 84]
        for i in range(len(fence)):
            if  fence[i][0] <x[0]< fence[i][2] and fence[i][1] <x[1]< fence[i][3]:
                break
            else:
                return x


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    game_window.blit(value, [0, 0])


pygame.init()
difficulty = 30  # сложность

score_font = pygame.font.SysFont("comicsansms", 15)

frame_size_x = 720  # размер поля по х
frame_size_y = 480

pygame.display.set_caption('Snake')  # название окна
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))  # размер окна

black = pygame.Color(0, 0, 0)  # цвета
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
pink = pygame.Color(255, 20, 147)

fps_controller = pygame.time.Clock()  # скорость игры

snake_pos = [100, 50]  # позиция головы змейки
snake_body = [[100, 50], [90, 50], [80, 50]]

fence = [[110, 84, 310, 84], [254, 252, 254, 398], [0, 424, 300, 424]]

food_pos = food_poss(frame_size_x, frame_size_y, fence)  # позиция яблока
food_pos_2 = food_poss(frame_size_x, frame_size_y, fence)
food_pos_3 = food_poss(frame_size_x, frame_size_y, fence)

food_spawn = False
food_spawn_2 = False
food_spawn_3 = False

direction = 'RIGHT'  # направление
change_to = direction  # изменение направления

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):  # ord проверяет двоичный код клавишь
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if change_to == 'UP' and direction != 'DOWN':
        direction = change_to
    if change_to == 'DOWN' and direction != 'UP':
        direction = change_to
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = change_to
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = change_to

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    elif snake_pos[0] == food_pos_2[0] and snake_pos[1] == food_pos_2[1]:
        score += 1
        food_spawn_2 = False
    elif snake_pos[0] == food_pos_3[0] and snake_pos[1] == food_pos_3[1]:
        score += 1
        food_spawn_3 = False
    else:
        snake_body.pop()

    # if score % 5 == 0 and score != 0 and :
    #     difficulty += 5

    if not food_spawn:
        food_pos = food_poss(frame_size_x, frame_size_y,fence)
        food_spawn = True
    elif not food_spawn_2:
        food_pos_2 = food_poss(frame_size_x, frame_size_y,fence)
        food_spawn_2 = True
    elif not food_spawn_3:
        food_pos_3 = food_poss(frame_size_x, frame_size_y,fence)
        food_spawn_3 = True

    game_window.fill(black)
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos_2[0], food_pos_2[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos_3[0], food_pos_3[1], 10, 10))

    for fe in range(len(fence)):
        pygame.draw.line(game_window, red, [fence[fe][0], fence[fe][1]], [fence[fe][2], fence[fe][3]], 10)

    for pos in snake_body:
        pygame.draw.rect(game_window, white, pygame.Rect(pos[0], pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x - 10:
        game_over(score)
        # snake_pos[0] = fram_size_x -10
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y - 10:
        game_over(score)

    # for fen in range(len(fence)):
    #     if fence[fen][0] <=snake_pos[0]<= fence[fen][2] and fence[fen][1] <=snake_pos[1]<= fence[fen][3]:
    #         game_over()
    # if fence[0][0] <= snake_pos[0] <= fence[0][2] and fence[0][1] <= snake_pos[1] <= fence[0][3] or fence[0][0] <= snake_pos[1] <= fence[0][2] and fence[0][1] <= snake_pos[0] <= fence[0][3]:
    #     game_over()
    if fence[0][0] <= snake_pos[0] <= fence[0][2] and fence[0][1] <= snake_pos[0] <= fence[0][3]\
            or fence[0][0] <= snake_pos[1] <= fence[0][2] and fence[0][1] <= snake_pos[0] <= fence[0][3]\
            or fence[0][0] <= snake_pos[0] <= fence[0][2] and fence[0][1] <= snake_pos[1] <= fence[0][3]\
            or fence[0][0] <= snake_pos[1] <= fence[0][2] and fence[0][1] <= snake_pos[1] <= fence[0][3]:
        game_over(score)
    # if fence[fen][0] <= snake_pos[0] <= fence[fen][2] and fence[fen][1] <= snake_pos[1] <= fence[fen][3]:
    #     game_over()
    for block in snake_body[3::]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over(score)

    Your_score(score)

    pygame.display.update()
    fps_controller.tick((difficulty))
