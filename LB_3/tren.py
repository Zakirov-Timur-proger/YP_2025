import pygame
import random
from pygame.draw import *

pygame.init()

# Размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Дом с привидениями")

# Цвета
l_gray = (50, 50, 50)
black = (0, 0, 0)
white = (200, 200, 200)
gray = (100, 100, 100)
d_gray = (30, 30, 30)
yellow = (80, 80, 0)
brown = (30, 15, 5)
blue = (80, 80, 100)

# --- Функции рисования ---
def draw_background():
    screen.fill(l_gray)
    screen.fill(black, (0, height // 2, width, height // 2))

    cloud_color = (70, 70, 70)
    ellipse(screen, cloud_color, (100, 50, 200, 80))
    ellipse(screen, cloud_color, (400, 80, 250, 90))
    ellipse(screen, cloud_color, (600, 40, 150, 70))

    circle(screen, white, (width - 100, 100), 50)

def draw_house(x, y, size):
    house_width = int(200 * size)
    house_height = int(150 * size)
    roof_height = int(30 * size)
    window_size = int(30 * size)
    pipe_width = int(10 * size)
    pipe_height = int(20 * size)
    balcony_height = int(10 * size)

    base_color = (30, 25, 0)
    rect(screen, base_color, (x, y, house_width, house_height))
    rect(screen, d_gray, (x, y + house_height // 2 - balcony_height // 2, house_width, balcony_height))
    rect(screen, brown, (x + 20, y + house_height - window_size - 10, window_size, window_size))
    rect(screen, yellow, (x + house_width - window_size - 20, y + house_height - window_size - 10, window_size, window_size))
    rect(screen, d_gray, (x, y - house_height // 2, house_width, house_height // 2))
    rect(screen, black, (x, y - roof_height - house_height // 2, house_width, roof_height))
    rect(screen, black, (x + 20, y - roof_height - house_height // 2 - pipe_height, pipe_width, pipe_height))

def draw_ghost(x, y, size):  # Итоговый код привидения
    body_width = int(60 * size)
    head_width = int(80 * size)
    body_height = int(80 * size)
    eye_size = int(6 * size)
    eye_offset_x = int(15 * size)
    eye_offset_y = int(20 * size)
    head_offset = int(20 * size)

    # Лицо (верхняя часть)
    ellipse(screen, white, (x - (head_width - body_width) // 2, y - head_offset, head_width, body_height // 2))

    # Тело (средняя часть)
    ellipse(screen, white, (x, y - (body_height // 4), body_width, body_height))

    # Глаза
    circle(screen, blue, (int(x + eye_offset_x), int(y + eye_offset_y - (body_height // 4))), eye_size)
    circle(screen, black, (int(x + eye_offset_x), int(y + eye_offset_y - (body_height // 4))), eye_size // 2)

    circle(screen, blue, (int(x + body_width - eye_offset_x), int(y + eye_offset_y - (body_height // 4))), eye_size)
    circle(screen, black, (int(x + body_width - eye_offset_x), int(y + eye_offset_y - (body_height // 4))), eye_size // 2)

# --- Основной цикл ---
running = True
clock = pygame.time.Clock()
FPS = 30

# Создаем дома
houses = []
num_houses = 3
for i in range(num_houses):
    x = random.randint(0, width - 200)
    y = random.randint(height // 2, height - 150)
    size = random.uniform(0.5, 1.2)
    houses.append((x, y, size))

# Создаем привидения
ghosts = []
num_ghosts = 5
for i in range(num_ghosts):
    x = random.randint(0, width - 50)
    y = random.randint(height // 2, height - 50)
    size = random.uniform(0.3, 0.7)
    ghosts.append((x, y, size))

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рисование
    draw_background()

    # Рисуем дома
    for x, y, size in houses:
        draw_house(x, y, size)

    # Рисуем привидения
    for x, y, size in ghosts:
        draw_ghost(x, y, size)

    pygame.display.flip()

pygame.quit()
