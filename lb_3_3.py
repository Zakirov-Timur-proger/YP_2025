import pygame
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))


def draw_pixel(surface, x, y, color):
    if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():
        surface.set_at((int(x), int(y)), color)


def draw_circle_manual(surface, center_x, center_y, radius, color):
    for y in range(int(center_y - radius), int(center_y + radius) + 1):
        for x in range(int(center_x - radius), int(center_x + radius) + 1):
            if math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2) <= radius:
                draw_pixel(surface, x, y, color)


def draw_ellipse_manual(surface, x, y, width, height, color):
    hw = width / 2
    hh = height / 2
    cx = x + hw
    cy = y + hh

    for py in range(int(y), int(y + height) + 1):
        for px in range(int(x), int(x + width) + 1):
            dx = (px - cx) / hw
            dy = (py - cy) / hh
            if dx * dx + dy * dy <= 1:
                draw_pixel(surface, px, py, color)


def draw_arc_manual(surface, x, y, width, height, start_angle, end_angle, color, thickness=1):
    hw = width / 2
    hh = height / 2
    cx = x + hw
    cy = y + hh

    for py in range(int(y), int(y + height) + 1):
        for px in range(int(x), int(x + width) + 1):
            dx = (px - cx) / hw
            dy = (py - cy) / hh
            angle = math.atan2(dy, dx)
            if (start_angle <= angle <= end_angle) and (0.9 <= dx * dx + dy * dy <= 1.1):
                draw_pixel(surface, px, py, color)


def draw_body(surface, x, y, width, height, color):
    draw_ellipse_manual(surface, x - width // 2, y - height // 2, width, height, color)


def draw_head(surface, x, y, size, color):
    draw_circle_manual(surface, x, y, size // 2, color)

    # глаза
    eye_size = size // 8
    draw_circle_manual(surface, x - size // 6, y - size // 10, eye_size, (255, 255, 255))
    draw_circle_manual(surface, x + size // 6, y - size // 10, eye_size, (255, 255, 255))


    pupil_size = eye_size // 2
    draw_circle_manual(surface, x - size // 6, y - size // 10, pupil_size, (0, 0, 0))
    draw_circle_manual(surface, x + size // 6, y - size // 10, pupil_size, (0, 0, 0))

    # нос
    nose_size = size // 12
    draw_circle_manual(surface, x, y + size // 10, nose_size, (255, 100, 100))

    # рот
    mouth_width = size // 3
    mouth_height = size // 10
    mouth_y = y + size // 4
    draw_arc_manual(surface,
                    x - mouth_width // 2,
                    mouth_y - mouth_height // 2,
                    mouth_width, mouth_height,
                    0.2, 2.94, (0, 0, 0))


def draw_ear(surface, x, y, width, height, color):
    draw_ellipse_manual(surface, x - width // 2, y - height // 2, width, height, color)
    inner_color = (color[0] // 2, color[1] // 2, color[2] // 2)
    draw_ellipse_manual(surface,
                        x - width // 3,
                        y - height // 3,
                        width * 2 // 3, height * 2 // 3,
                        inner_color)


def draw_leg(surface, x, y, width, height, color):
    draw_ellipse_manual(surface, x - width // 2, y - height // 2, width, height, color)


def draw_hare(surface, x, y, width, height, color):
    # Body
    body_width = width // 2
    body_height = height // 2
    body_y = y + body_height // 2
    draw_body(surface, x, body_y, body_width, body_height, color)

    # Head
    head_size = height // 4
    draw_head(surface, x, y - head_size // 2, head_size, color)

    # Ears
    ear_height = height // 3
    ear_y = y - height // 2 + ear_height // 2
    draw_ear(surface, x - head_size // 4, ear_y, width // 8, ear_height, color)
    draw_ear(surface, x + head_size // 4, ear_y, width // 8, ear_height, color)

    # Legs
    leg_height = height // 16
    leg_y = y + height // 2 - leg_height // 2
    draw_leg(surface, x - width // 4, leg_y, width // 4, leg_height, color)
    draw_leg(surface, x + width // 4, leg_y, width // 4, leg_height, color)


# Draw hare
draw_hare(screen, 250, 250, 200, 400, (200, 200, 200))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()