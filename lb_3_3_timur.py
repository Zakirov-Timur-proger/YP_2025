import pygame
import math

# Constants
SCREEN_SIZE = (500, 500)
FPS = 30
HARE_COLOR = (200, 200, 200)
BACKGROUND_COLOR = (255, 255, 255)


def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill(BACKGROUND_COLOR)
    return screen


def draw_pixel(surface, x, y, color):
    """Draw a single pixel on the surface if coordinates are valid"""
    if 0 <= x < surface.get_width() and 0 <= y < surface.get_height():
        surface.set_at((int(x), int(y)), color)


def draw_circle(surface, center_x, center_y, radius, color):
    """Draw a circle using pixel-by-pixel method"""
    for y in range(int(center_y - radius), int(center_y + radius) + 1):
        for x in range(int(center_x - radius), int(center_x + radius) + 1):
            if math.hypot(x - center_x, y - center_y) <= radius:
                draw_pixel(surface, x, y, color)


def draw_ellipse(surface, x, y, width, height, color):
    """Draw an ellipse using pixel-by-pixel method"""
    half_w = width / 2
    half_h = height / 2
    center_x = x + half_w
    center_y = y + half_h

    for py in range(int(y), int(y + height) + 1):
        for px in range(int(x), int(x + width) + 1):
            dx = (px - center_x) / half_w
            dy = (py - center_y) / half_h
            if dx * dx + dy * dy <= 1:
                draw_pixel(surface, px, py, color)


def draw_arc(surface, x, y, width, height, start_angle, end_angle, color, thickness=1):
    """Draw an arc using pixel-by-pixel method"""
    half_w = width / 2
    half_h = height / 2
    center_x = x + half_w
    center_y = y + half_h

    for py in range(int(y), int(y + height) + 1):
        for px in range(int(x), int(x + width) + 1):
            dx = (px - center_x) / half_w
            dy = (py - center_y) / half_h
            angle = math.atan2(dy, dx)
            if (start_angle <= angle <= end_angle) and (0.9 <= dx * dx + dy * dy <= 1.1):
                draw_pixel(surface, px, py, color)


def draw_head(surface, x, y, size, color):
    """Draw the hare's head with eyes, nose and mouth"""
    # Head base
    draw_circle(surface, x, y, size // 2, color)

    # Eyes
    eye_size = size // 8
    eye_y = y - size // 10
    for eye_x in (x - size // 6, x + size // 6):
        draw_circle(surface, eye_x, eye_y, eye_size, (255, 255, 255))
        draw_circle(surface, eye_x, eye_y, eye_size // 2, (0, 0, 0))

    # Nose
    draw_circle(surface, x, y + size // 10, size // 12, (255, 100, 100))

    # Mouth (smile)
    mouth_width = size // 3
    mouth_height = size // 10
    draw_arc(surface,
             x - mouth_width // 2,
             y + size // 4 - mouth_height // 2,
             mouth_width, mouth_height,
             0.2, 2.94, (0, 0, 0))


def draw_ear(surface, x, y, width, height, color):
    """Draw the hare's ear with inner part"""
    # Изменяем форму уха, чтобы оно было более прижатым
    draw_ellipse(surface, x - width // 2, y - height // 2, width, height * 0.7, color)
    inner_color = tuple(c // 2 for c in color)  # Darker version of main color
    draw_ellipse(surface,
                 x - width // 3,
                 y - height // 3,
                 width * 2 // 3, height * 0.7 * 2 // 3,
                 inner_color)


def draw_hare(surface, center_x, center_y, width, height, color):
    """Draw a complete hare at specified position and size"""
    # Body
    body_y = center_y + height // 4
    draw_ellipse(surface,
                 center_x - width // 4,
                 body_y - height // 4,
                 width // 2, height // 2,
                 color)

    # Head
    head_y = center_y
    head_size = height // 4
    draw_head(surface, center_x, head_y, head_size, color)

    # Ears - теперь уши ближе к голове и более прижатые
    ear_y = center_y - height // 4  # Подняли уши выше
    ear_height = height // 4  # Уменьшили высоту ушей
    for ear_x in (center_x - width // 6, center_x + width // 6):  # Уши ближе к голове
        draw_ear(surface, ear_x, ear_y, width // 6, ear_height, color)

    # Legs
    leg_y = center_y + height // 2 - height // 32
    for leg_x in (center_x - width // 4, center_x + width // 4):
        draw_ellipse(surface,
                     leg_x - width // 8,
                     leg_y - height // 32,
                     width // 4, height // 16,
                     color)


def main():
    """Main program loop"""
    screen = init_pygame()
    draw_hare(screen, 250, 250, 200, 400, HARE_COLOR)
    pygame.display.update()

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()


if __name__ == "__main__":
    main()