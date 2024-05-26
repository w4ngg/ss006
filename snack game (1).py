from pygame import *
import pygame
import time
import random
 


 
# chieu dai va chieu rong cua background
window_x = 900
window_y = 800
 
# RGB colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
 
# khai bao pygame
pygame.init()

# khai bao game window
pygame.display.set_caption('Snacks Game')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS cho tro choi (frame per second)
fps = pygame.time.Clock()
 
 
# vi tri ban dau cua con ran khi bat dau tro choi
snake_position = [100, 50]
 
# than con ran
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# toc do di chuyen cua con ran
snake_speed = 15
# huong ban dau cua con ran khi tro choi bat dau
direction = 'RIGHT'
change_to = direction


# tao vi tri cho cac buc tuong
wall = [[500, 400],[510,400],[520,400],[530,400],[540,400],[550, 400],[560,400],[570,400],[580,400],[590,400],[600,400]]


wall1 = [[700, 200],[700,210],[700,220],[700,230],[700,240],[700,250],[700, 260],[700,270],[700,280],[700,290],[700,300],[700,310],
         [710, 200],[720, 200],[730, 200],[740, 200],[750, 200],[760, 200],[770, 200],[780, 200],[790, 200],[800, 200],[810, 200]]


wall2= [[100, 100],[100, 110],[100,120],[100,130],[100,140],[100, 150],[100, 160],[100,170],[100,180],[100,190],[100,200],
        [90, 200],[80, 200],[70, 200],[60, 200],[50, 200],[40, 200],[30, 200],[20, 200],[10, 200],
        [110,200],[120,200],[130,200],[140,200],[150,200],[160,200],[170,200],[180,200],[190,200]]


wall3 = [[300, 600],[300,610],[300,620],[300,630],[300,640],[300, 650],[300,660],[300,670],[300,680],[300,690],[300,700],
         [300, 590],[300, 580],[300, 570],[300, 560],[300, 550],
         [290, 550],[280, 550],[270, 550],[260, 550],[250, 550],[240, 550],[230, 550],[220, 550],[210, 550],[200, 550],[190, 550],[180, 550],[170, 550],
         [310, 550],[320, 550],[330, 550],[340, 550],[350, 550],[360, 550],[370, 550],[380, 550],[390, 550],[400, 550],[410, 550],[420, 550],[430, 550],
         [430, 540],[430, 530],[430, 520],[430, 510],[430, 500],[430, 490],[430, 480],
         [420, 480],[410, 480],[400, 480],[390, 480],[380, 480],[370, 480],[360, 480],[350,480],
         [350,470],[350,460],[350,450],[350,440],[350,450],[350,440],[350,430],[350,420],[350,410],[350,400],[350,390],[350,380]]


wall4 = [[600, 450],[600,460],[600,470],[600,480],[600,490],[600, 500],[600,510],[600,520],[600,530],[600,540],
         [610, 450],[620, 450],[630, 450],[640, 450],[650, 450],[660, 450],[670, 450],[680, 450],[690, 450],[700, 450]]


# random vi tri fruit
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]
#check coi co fruit tren ban do khongg
fruit_spawn = True
 

# khai bao diem
score = 0
# ham hien diem
def show_score(choice, color, font, size):
   
    # set up font and size cho score
    score_font = pygame.font.SysFont(font, size)
   # ghep chu "Score" va hien mau cho chu
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # tao ra 1 cai khung cho chu "Score"
    score_rect = score_surface.get_rect()
    # displaying text
    game_window.blit(score_surface, score_rect)
 
#  losing condition
def game_over():
    # set font chu va size 
    my_font = pygame.font.SysFont('times new roman', 50)
    # Hien thi so diem
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    # tao khung cho chu
    game_over_rect = game_over_surface.get_rect()
    # vi tri cua chu
    game_over_rect.midtop = (window_x/2, window_y/4)
    # hien thi chu ra man hinh
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    # sau khi thua chuong trinh close trong 2 giay
    time.sleep(2)
    # vo hieu hoa pygame
    pygame.quit()
    quit()
 
 
#  main function
while True:
     
    # ham set key dieu khien con ran
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # neu 2 phim cung duoc nhan thi chi nhan 1 huong di
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # dieu khien con ran
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Khi an fruit thi tang co dai va + 10 diem
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()


    # check fruit co hien thi khong
    # check fruit co trung vi tri voi buc tuong khong
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        for pos in wall:
            if fruit_position == pos[0] and fruit_position[1] == pos[1]:
                fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        
        for pos in wall1:
            if fruit_position == pos[0] and fruit_position[1] == pos[1]:
                fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        
        for pos in wall2:
            if fruit_position == pos[0] and fruit_position[1] == pos[1]:
                fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
                
        for pos in wall3:
            if fruit_position == pos[0] and fruit_position[1] == pos[1]:
                fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        
        for pos in wall4:
            if fruit_position == pos[0] and fruit_position[1] == pos[1]:
                fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]

        
    fruit_spawn = True

    # Hien thi background mau den
    game_window.fill(black)
    # Hien thi con ran mau xanh
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    # Hien thi con ran mau xanh la ra man hinh  
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    
    # Hien thi 4 buc tuong
    for posi in wall:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(posi[0], posi[1], 10, 10))

    for posi in wall1:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(posi[0], posi[1], 10, 10))

    for posi in wall2:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(posi[0], posi[1],10, 10))
    for posi in wall3:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(posi[0], posi[1], 10, 10))
    for posi in wall4:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(posi[0], posi[1], 10, 10))
        
    # Check con ran co va cham voi khung
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Con ran va cham chinh no
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    #  Con ran va cham buc tuong
    for pos in wall:
            if snake_position[0] == pos[0] and snake_position[1] == pos[1]:
                game_over()

    for pos in wall1:
            if snake_position[0] == pos[0] and snake_position[1] == pos[1]:
                game_over()
    
    for pos in wall2:
            if snake_position[0] == pos[0] and snake_position[1] == pos[1]:
                game_over()
    
    for pos in wall3:
            if snake_position[0] == pos[0] and snake_position[1] == pos[1]:
                game_over()
                
    for pos in wall4:
            if snake_position[0] == pos[0] and snake_position[1] == pos[1]:
                game_over()


    # Hien diem 
    show_score(1, white, 'times new roman', 20)
 
    # renew the game
    pygame.display.update()
 
    # FPS
    fps.tick(snake_speed)