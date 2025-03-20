import pygame

pygame.init()

# Размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Дом с призраком и облаками")

# Цвета
l_gray = (50, 50, 50)  # Темнее
black = (0, 0, 0)  # Черный
white = (200, 200, 200)  # Светлее
gray = (100, 100, 100)  # Темнее
d_gray = (30, 30, 30)  # Темнее
yellow = (80, 80, 0)  # Более приглушенный
brown = (30, 15, 5)  # Темнее
beige = (150, 150, 130)  # Более тусклый
blue = (80, 80, 100)  # Более приглушенный

# Функция для рисования фона
def draw_background():
    # Верхняя половина светло-серого цвета
    screen.fill(l_gray, (0, 0, width, height // 2))
    # Нижняя половина черного цвета
    screen.fill(black, (0, height // 2, width, height // 2))

    # Облака (овалы темно-серого и серого цветов)
    cloud_color = (70,70,70)
    pygame.draw.ellipse(screen, cloud_color, (100, 50, 200, 80))
    pygame.draw.ellipse(screen, cloud_color, (400, 80, 250, 90))
    pygame.draw.ellipse(screen, cloud_color, (600, 40, 150, 70))

    # Белый круг в верхней правой части (луна)
    pygame.draw.circle(screen, white, (width - 100, 100), 50)

def draw_house(x, y):
    house_width = 200  # Меньше ширина дома
    house_height = 150 # Меньше высота дома
    roof_height = 30   # Меньше высота крыши
    window_size = 30  # Меньше размер окон
    pipe_width = 10
    pipe_height = 20
    balcony_height = 10

    base_color = (30, 25, 0)  # Коричневатый цвет для дома
    # Основание дома
    pygame.draw.rect(screen, base_color, (x, y, house_width, house_height))

    # Балкон
    pygame.draw.rect(screen, d_gray, (x, y + house_height // 2 - balcony_height // 2, house_width, balcony_height))

    # Окна первого этажа (всего 3 окна)
    pygame.draw.rect(screen, brown, (x + 20, y + house_height - window_size - 10, window_size, window_size)) #Левое окно
    #pygame.draw.rect(screen, brown, (x + house_width//2 - window_size//2, y + house_height - window_size - 10, window_size, window_size)) #Среднее окно #Remove the middle one

    pygame.draw.rect(screen, yellow, (x + house_width - window_size - 20, y + house_height - window_size - 10, window_size, window_size)) #Правое окно

    # Второй этаж (без окон)
    pygame.draw.rect(screen, d_gray, (x, y- house_height // 2, house_width, house_height//2 )) #Cерый этаж

    # Крыша (простой прямоугольник)
    pygame.draw.rect(screen, black, (x, y - roof_height - house_height // 2, house_width, roof_height))#Крыша

    # Трубы (упрощенные)
    pygame.draw.rect(screen, black,
                     (x + 20, y - roof_height - house_height // 2 - pipe_height, pipe_width, pipe_height))
    # pygame.draw.rect(screen, black, (x + house_width - 30, y - roof_height - house_height // 2 - pipe_height, pipe_width, pipe_height)) ##Remove 2nd pipe


def draw_ghost(x, y):
    body_width = 60  # Призрак поменьше
    body_height = 80
    eye_size = 6  # Глаз тоже
    eye_offset_x = 15
    eye_offset_y = 20  # Глаз поближе к верху
    skirt_length = 20  # Длина юбки

    # Тело
    pygame.draw.ellipse(screen, white, (x, y, body_width, body_height))

    # многоугольник
    pygame.draw.polygon(screen, gray, [
        (x, y + body_height),
        (x + body_width, y + body_height),
        (x + body_width + skirt_length, y + body_height + skirt_length),
        (x - skirt_length, y + body_height + skirt_length)
    ])

    # Глаза
    pygame.draw.circle(screen, blue, (x + eye_offset_x, y + eye_offset_y), eye_size)
    pygame.draw.circle(screen, black, (x + eye_offset_x, y + eye_offset_y), eye_size // 2)

    pygame.draw.circle(screen, blue, (x + body_width - eye_offset_x, y + eye_offset_y), eye_size)
    pygame.draw.circle(screen, black, (x + body_width - eye_offset_x, y + eye_offset_y), eye_size // 2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка фона
    draw_background()

    # Рисование дома (в разных местах)
    draw_house(50, height - 350)
    draw_house(300, height - 300)  # Второй дом, чуть правее и выше
    draw_house(550, height - 400)  # Третий дом, еще правее и выше

    # Рисование призрака (в разных местах)
    draw_ghost(150, height - 180)
    draw_ghost(250, height - 150)  # Второй призрак
    draw_ghost(600, height - 100)
    draw_ghost(700, height - 80)  # 4 призрак

    pygame.display.flip()

pygame.quit()
