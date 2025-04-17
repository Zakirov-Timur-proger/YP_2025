import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((135, 206, 235))  # Небесно-голубой фон


def draw_body(surface, x, y, width, height, color):
    """Рисует тело кролика в виде эллипса"""
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_head(surface, x, y, size, color):
    """Рисует голову кролика в виде круга"""
    circle(surface, color, (x, y), size)


def draw_ear(surface, x, y, width, height, color, pink_color):
    """Рисует ухо кролика с розовой внутренней частью"""
    # Внешняя часть уха
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))
    # Внутренняя розовая часть
    inner_width = width // 2
    inner_height = height * 7 // 8
    ellipse(surface, pink_color,
            (x - inner_width // 2, y - inner_height // 2 + height // 8,
             inner_width, inner_height))


def draw_leg(surface, x, y, width, height, color, pink_color):
    """Рисует лапу кролика с розовой подушечкой"""
    # Основная часть лапы
    ellipse(surface, color, (x - width // 2, y - height // 2, width, height))
    # Подушечка лапы
    pad_width = width // 2
    pad_height = height // 3
    ellipse(surface, pink_color,
            (x - pad_width // 2, y + height // 4 - pad_height // 2,
             pad_width, pad_height))


def draw_face(surface, x, y, head_size):
    """Рисует мордочку кролика (глаза, рот, усы)"""
    # Глаза
    eye_size = head_size // 4
    for dx in (-1, 1):
        circle(surface, (0, 0, 0), (x + dx * head_size // 3, y - head_size // 6), eye_size)

    # Рот
    line(surface, (0, 0, 0), (x - head_size // 5, y + head_size // 6),
         (x + head_size // 5, y + head_size // 6), 2)

    # Усы
    for dx in (-1, 1):
        for dy in (-1, 0, 1):
            line(surface, (0, 0, 0),
                 (x + dx * head_size // 3, y),
                 (x + dx * head_size // 1.5, y + dy * head_size // 4), 1)


def draw_rabbit(surface, x, y, width, height):
    """Рисует всего кролика в заданной позиции и размерах"""
    color = (220, 220, 220)  # Серый цвет тела
    pink_color = (255, 182, 193)  # Розовый цвет

    # Тело
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 4
    draw_body(surface, x, body_y, body_width, body_height, color)

    # Голова
    head_size = height // 4
    head_y = y - head_size // 2
    draw_head(surface, x, head_y, head_size, color)

    # Уши
    ear_width = width // 4
    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    for ear_x in (x - head_size // 2, x + head_size // 2):
        draw_ear(surface, ear_x, ear_y, ear_width, ear_height, color, pink_color)

    # Задние лапы
    hind_leg_width = width // 3
    hind_leg_height = height // 5
    for leg_x in (x - width // 3, x + width // 3):
        draw_leg(surface, leg_x, y + height // 3,
                 hind_leg_width, hind_leg_height, color, pink_color)

    # Передние лапы
    front_leg_width = width // 4
    front_leg_height = height // 6
    for leg_x in (x - width // 6, x + width // 6):
        draw_leg(surface, leg_x, y + height // 6,
                 front_leg_width, front_leg_height, color, pink_color)

    # Мордочка
    draw_face(surface, x, head_y, head_size)


# Рисуем кролика
draw_rabbit(screen, 200, 200, 200, 400)

pygame.display.update()
while True:
    if any(e.type == pygame.QUIT for e in pygame.event.get()):
        break
pygame.quit()