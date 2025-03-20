import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
shir = 600
vis = 600
screen = pygame.display.set_mode((shir, vis))
pygame.display.set_caption("smile")

# Цвета
gray = (200, 200, 200)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)

# Координаты и размеры (упрощенные)
face_x =  shir// 2
face_y = vis // 2
face_radius = 200
eye_radius_left = 40  # Левый глаз больше
eye_radius_right = 30 # Правый глаз меньше
eye_distance = 95
mouth_width = 200    # Рот шире
mouth_height = 40
eyebrow_thickness = 20
eyebrow_angle = 150

eyebrow_length_left = 150
eyebrow_length_right = 100 # Правая бровь короче


# Функция для рисования брови
def draw_eyebrow(x, y, angle, length):  # Добавили аргумент length
    x1 = x - length / 2
    y1 = y
    x2 = x + length / 2
    y2 = y
    rotated_start = pygame.math.Vector2(x1 - x, y1 - y).rotate(angle) + (x, y)
    rotated_end = pygame.math.Vector2(x2 - x, y2 - y).rotate(angle) + (x, y)
    pygame.draw.line(screen, black, rotated_start, rotated_end, eyebrow_thickness)


# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(gray)

    # Рисуем лицо
    pygame.draw.circle(screen, yellow, (face_x, face_y), face_radius)
    pygame.draw.circle(screen, black, (face_x, face_y), face_radius, 3)

    # Рисуем глаза (разного размера)
    pygame.draw.circle(screen, red, (face_x - eye_distance, face_y - 50), eye_radius_left)  # Левый глаз
    pygame.draw.circle(screen, black, (face_x - eye_distance, face_y - 50), eye_radius_left, 3)
    pygame.draw.circle(screen, black, (face_x - eye_distance, face_y - 50), eye_radius_left//2)

    pygame.draw.circle(screen, red, (face_x + eye_distance, face_y - 50), eye_radius_right) # Правый глаз
    pygame.draw.circle(screen, black, (face_x + eye_distance, face_y - 50), eye_radius_right, 3)
    pygame.draw.circle(screen, black, (face_x + eye_distance, face_y - 50), eye_radius_right//2)


    # Рисуем рот (шире)
    pygame.draw.rect(screen, black, (face_x - mouth_width / 2, face_y + 80, mouth_width, mouth_height))

    # Рисуем брови (с разной длиной)
    draw_eyebrow(face_x - eye_distance, face_y - 100, -eyebrow_angle, eyebrow_length_left) # Левая бровь
    draw_eyebrow(face_x + eye_distance, face_y - 90, eyebrow_angle, eyebrow_length_right)  # Правая бровь

    pygame.display.flip()

pygame.quit()
