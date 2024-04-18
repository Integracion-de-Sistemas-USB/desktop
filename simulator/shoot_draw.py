import pygame
from peripheral.constants import (
    HALF,
    ZERO,
    POINTER_LOW_SIZE,
    POINTER_MEDIUM_SIZE,
    POINTER_HIGH_SIZE,
    POINTER_SIZE
)
from simulator.target_draw import calculate_distance

def draw_peripheral_pointer(pointer_position, color, screen):
    if pointer_position != None:
        w, h = screen.get_size()
        x = min(max((pointer_position[0] * w / HALF + screen.get_rect().centerx), ZERO), w)
        y = min(max((-pointer_position[1] * h / HALF + screen.get_rect().centery), ZERO), h)
        pygame.draw.circle(screen, color, (x, y), POINTER_SIZE)

def draw_shoot(pointer_position, color, screen, stress):
    x = pointer_position[0]
    y = pointer_position[1]
    if calculate_distance(stress) == 10:
        pygame.draw.circle(screen, color, (x, y), POINTER_LOW_SIZE)
    if calculate_distance(stress) == 20:
        pygame.draw.circle(screen, color, (x, y), POINTER_MEDIUM_SIZE)
    else:
        pygame.draw.circle(screen, color, (x, y), POINTER_HIGH_SIZE)

def draw_shoots(red_points, color, screen, stress):
    for point in red_points:
        draw_shoot(point, color, screen, stress)
