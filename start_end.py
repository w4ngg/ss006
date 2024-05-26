from pygame import *
import pygame
import time
import random

# Tốc độ của con rắn
snake_speed = 15

# Chiều dài và chiều rộng của background
window_x = 900
window_y = 800

# Màu RGB
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Khai báo pygame
pygame.init()
start_bg = transform.scale(image.load('start_bg.png'), (window_x, window_y))
end_bg = transform.scale(image.load('end_bg.png'), (window_x, window_y))
start_sound = pygame.mixer.Sound('start_sound.mp3')
eat_sound = pygame.mixer.Sound('eat.mp3')
end_sound = pygame.mixer.Sound('end_sound.wav.mp3')
# Khai báo game window
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS cho trò chơi (frame per second)
fps = pygame.time.Clock()

# Vị trí ban đầu của con rắn khi trò chơi bắt đầu
snake_position = [100, 50]

# Tạo ra 4 khối liên tiếp để có thân con rắn
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# Tạo ra list vị trí cho từng chướng ngại vật
wall = [[500, 400], [510, 400], [520, 400], [530, 400], [540, 400], [550, 400], [560, 400], [570, 400], [580, 400], [590, 400], [600, 400]]
wall1 = [[700, 200], [700, 210], [700, 220], [700, 230], [700, 240], [700, 250], [700, 260], [700, 270], [700, 280], [700, 290], [700, 300], [700, 310],
         [710, 200], [720, 200], [730, 200], [740, 200], [750, 200], [760, 200], [770, 200], [780, 200], [790, 200], [800, 200], [810, 200]]
wall2 = [[100, 100], [100, 110], [100, 120], [100, 130], [100, 140], [100, 150], [100, 160], [100, 170], [100, 180], [100, 190], [100, 200],
         [90, 200], [80, 200], [70, 200], [60, 200], [50, 200], [40, 200], [30, 200], [20, 200], [10, 200],
         [110, 200], [120, 200], [130, 200], [140, 200], [150, 200], [160, 200], [170, 200], [180, 200], [190, 200]]
wall3 = [[300, 600], [300, 610], [300, 620], [300, 630], [300, 640], [300, 650], [300, 660], [300, 670], [300, 680], [300, 690], [300, 700],
         [300, 590], [300, 580], [300, 570], [300, 560], [300, 550],
         [290, 550], [280, 550], [270, 550], [260, 550], [250, 550], [240, 550], [230, 550], [220, 550], [210, 550], [200, 550], [190, 550], [180, 550], [170, 550],
         [310, 550], [320, 550], [330, 550], [340, 550], [350, 550], [360, 550], [370, 550], [380, 550], [390, 550], [400, 550], [410, 550], [420, 550], [430, 550],
         [430, 540], [430, 530], [430, 520], [430, 510], [430, 500], [430, 490], [430, 480],
         [420, 480], [410, 480], [400, 480], [390, 480], [380, 480], [370, 480], [360, 480], [350, 480],
         [350, 470], [350, 460], [350, 450], [350, 440], [350, 450], [350, 440], [350, 430], [350, 420], [350, 410], [350, 400], [350, 390], [350, 380]]
wall4 = [[600, 450], [600, 460], [600, 470], [600, 480], [600, 490], [600, 500], [600, 510], [600, 520], [600, 530], [600, 540],
         [610, 450], [620, 450], [630, 450], [640, 450], [650, 450], [660, 450], [670, 450], [680, 450], [690, 450], [700, 450]]

# Random vị trí của trái táo
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
# Check coi có fruit trên bản đồ không
fruit_spawn = True

# Hướng ban đầu của con rắn khi trò chơi bắt đầu
direction = 'RIGHT'
change_to = direction
# Khai báo điểm
score = 0

# Hàm hiện điểm
def show_score(choice, color, font, size):
    # Set up font và size cho score
    score_font = pygame.font.SysFont(font, size)
    # Ghép chữ "Score" và điểm, set màu cho chữ
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # Tạo ra 1 cái khung để chữ score
    score_rect = score_surface.get_rect()
    # Displaying text
    game_window.blit(score_surface, score_rect)

# Hàm game over
def game_over():
    # Gọi hàm end_game
    end_game()

# Hàm bắt đầu trò chơi
def start_game():
    start_sound.play()
    while True:
        game_window.fill(black)
        font = pygame.font.SysFont('times new roman', 50)
        welcome_surface = font.render('Welcome to Snake Game', True, white)
        instruction_surface = font.render('Press SPACE to start', True, white)
        welcome_rect = welcome_surface.get_rect()
        instruction_rect = instruction_surface.get_rect()
        welcome_rect.midtop = (window_x / 2, window_y / 4)
        instruction_rect.midtop = (window_x / 2, window_y / 2)
        game_window.blit(welcome_surface, welcome_rect)
        game_window.blit(instruction_surface, instruction_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_sound.stop()
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

# Hàm kết thúc trò chơi
def end_game():
    end_sound.play()
    while True:
        game_window.fill(black)
        font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = font.render('Your Score is : ' + str(score), True, red)
        instruction_surface = font.render('Press ESC to quit', True, white)
        game_over_rect = game_over_surface.get_rect()
        instruction_rect = instruction_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        instruction_rect.midtop = (window_x / 2, window_y / 2)
        game_window.blit(game_over_surface, game_over_rect)
        game_window.blit(instruction_surface, instruction_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end_sound.stop()
                    pygame.quit()
                    quit()

# Hàm main
start_game()
while True:
    # Hàm set key để điều khiển nhân vật
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

    # Nếu 2 phím được nhấn cùng 1 lúc chỉ định 1 hướng cho rắn đi
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Điều khiển con rắn
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Tăng độ dài cơ thể con rắn khi nó ra chạm với thức ăn và tăng điểm lên 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        eat_sound.play()
        fruit_spawn = False
    else:
        snake_body.pop()

    # Check coi fruit có hiển thị không
    # Check fruit có trùng vị trí với chướng ngại vật không
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
        for pos in wall:
            if fruit_position == pos[0] and fruit_position[1] == pos[1]:
                fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                                  random.randrange(1, (window_y // 10)) * 10]

        for pos in wall1:
            if fruit_position == pos[0] and fruit_position[1] == pos[1]:
                fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                                  random.randrange(1, (window_y // 10)) * 10]

        for pos in wall2:
            if fruit_position == pos[0] and fruit_position[1] == pos[1]:
                fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                                  random.randrange(1, (window_y // 10)) * 10]

        for pos in wall3:
            if fruit_position == pos[0] and fruit_position[1] == pos[1]:
                fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                                  random.randrange(1, (window_y // 10)) * 10]

        for pos in wall4:
            if fruit_position == pos[0] and fruit_position[1] == pos[1]:
                fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                                  random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True

    # Hiển thị background màu đen
    game_window.fill(black)
    # Hiển thị con rắn màu xanh ra màn hình
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    # Hiển thị fruit ra màn hình
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Hiển thị 4 bức tường
    for posi in wall:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(posi[0], posi[1], 10, 10))

    for posi in wall1:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(posi[0], posi[1], 10, 10))

    for posi in wall2:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(posi[0], posi[1], 10, 10))
    for posi in wall3:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(posi[0], posi[1], 10, 10))
    for posi in wall4:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(posi[0], posi[1], 10, 10))

    # Check con rắn có va chạm khung
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Con rắn va chạm với thân
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Con rắn va chạm với chướng ngại vật
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

    # Hiện điểm
    show_score(1, white, 'times new roman', 20)

    # Làm mới lại trò chơi
    pygame.display.update()

    # FPS
    fps.tick(snake_speed)
