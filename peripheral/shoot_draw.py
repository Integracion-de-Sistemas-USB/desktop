import pygame
from .constants import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_peripheral_pointer(pointer_position, color):
    x = min(max(int(pointer_position[0] * WIDTH / 2 + WIDTH / 2), 0), WIDTH)
    y = min(max(int(-pointer_position[1] * HEIGHT / 2 + HEIGHT / 2), 0), HEIGHT)
    pygame.draw.circle(screen, color, (x, y), POINTER_SIZE)

def draw_mouse_pointer(pointer_position, color):
    x = pointer_position[0]
    y = pointer_position[1]
    pygame.draw.circle(screen, color, (x, y), POINTER_SIZE)

def draw_shoots(red_points, color, peripheral):
    for point in red_points:
        if peripheral:
            draw_peripheral_pointer(point, color)
        else:
            draw_mouse_pointer(point, color)
