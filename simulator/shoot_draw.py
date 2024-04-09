import pygame
from peripheral.constants import (
    HALF, 
    WIDTH, 
    HEIGHT, 
    POINTER_SIZE, 
    ZERO
)

def draw_peripheral_pointer(pointer_position, color, screen):
    if pointer_position != None:
        x = min(max((pointer_position[0] * WIDTH / HALF + screen.get_rect().centerx), ZERO), WIDTH)
        y = min(max((-pointer_position[1] * HEIGHT / HALF + screen.get_rect().centery), ZERO), HEIGHT)
        pygame.draw.circle(screen, color, (x, y), POINTER_SIZE)

def draw_mouse_pointer(pointer_position, color, screen):
    x = pointer_position[0]
    y = pointer_position[1]
    pygame.draw.circle(screen, color, (x, y), POINTER_SIZE)

def draw_shoots(red_points, color, peripheral, screen):
    for point in red_points:
        if peripheral:
            draw_peripheral_pointer(point, color, screen)
        else:
            draw_mouse_pointer(point, color, screen)
