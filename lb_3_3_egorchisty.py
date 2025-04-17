import pygame
import math
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((135, 206, 235))  # Небесно-голубой фон


def draw_circle(surface, color, center, radius):

    x0, y0 = center
    for y in range(int(y0 - radius), int(y0 + radius) + 1):
        for x in range(int(x0 - radius), int(x0 + radius) + 1):
            if (x - x0) ** 2 + (y - y0) ** 2 <= radius ** 2:
                if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():
                    surface.set_at((x, y), color)


def draw_ellipse(surface, color, rect):

    x, y, width, height = rect
    a = width / 2
    b = height / 2
    center_x = x + a
    center_y = y + b

    for dy in range(int(-b), int(b) + 1):
        for dx in range(int(-a), int(a) + 1):
            if (dx / a) ** 2 + (dy / b) ** 2 <= 1:
                px = int(center_x + dx)
                py = int(center_y + dy)
                if 0 <= px < surface.get_width() and 0 <= py < surface.get_height():
                    surface.set_at((px, py), color)


def draw_body(surface, x, y, width, height, color):

    draw_ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_head(surface, x, y, size, color):

    draw_circle(surface, color, (x, y), size)


def draw_ear(surface, x, y, width, height, color, pink_color):

    # Внешняя часть уха
    draw_ellipse(surface, color, (x - width // 2, y - height // 2, width, height))


def draw_leg(surface, x, y, width, height, color, pink_color):

    # Основная часть лапы
    draw_ellipse(surface, color, (x - width // 2, y - height // 2, width, height))
    # Подушечка лапы
    pad_width = width // 2
    pad_height = height // 3
    draw_ellipse(surface, pink_color,
                 (x - pad_width // 2, y + height // 4 - pad_height // 2,
                  pad_width, pad_height))


def draw_face(surface, x, y, head_size):

    # Глаза
    eye_size = head_size // 4
    for dx in (-1, 1):
        draw_circle(surface, (0, 0, 0), (x + dx * head_size // 3, y - head_size // 6), eye_size)

    # Рот
    pygame.draw.line(surface, (0, 0, 0), (x - head_size // 5, y + head_size // 6),
                     (x + head_size // 5, y + head_size // 6), 2)


def draw_rabbit(surface, x, y, width, height):

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

    draw_face(surface, x, head_y, head_size)

draw_rabbit(screen, 200, 200, 200, 400)

pygame.display.update()
while True:
    if any(e.type == pygame.QUIT for e in pygame.event.get()):
        break
pygame.quit()