import pygame
from peripheral.constants import (
    HALF, 
    POINTER_SIZE, 
    ZERO
)

def draw_peripheral_pointer(pointer_position, color, screen):
    if pointer_position != None:
        w, h = screen.get_size()
        x = min(max((pointer_position[0] * w / HALF + screen.get_rect().centerx), ZERO), w)
        y = min(max((-pointer_position[1] * h / HALF + screen.get_rect().centery), ZERO), h)
        pygame.draw.circle(screen, color, (x, y), POINTER_SIZE)

def draw_shoot(pointer_position, color, screen):
    x = pointer_position[0]
    y = pointer_position[1]
    pygame.draw.circle(screen, color, (x, y), POINTER_SIZE)

def draw_shoots(red_points, color, screen):
    for point in red_points:
        draw_shoot(point, color, screen)
