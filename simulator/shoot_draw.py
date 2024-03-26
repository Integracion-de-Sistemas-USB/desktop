import pygame
from peripheral.constants import (
    HALF, 
    WIDTH, 
    HEIGHT, 
    POINTER_SIZE, 
    ZERO
)
from form.form_module import form_built_flag

form_built_flag.wait()

def draw_peripheral_pointer(pointer_position, color, screen):
    if pointer_position != None:
        x = min(max(int(pointer_position[0] * WIDTH / HALF + WIDTH / HALF), ZERO), WIDTH)
        y = min(max(int(-pointer_position[1] * HEIGHT / HALF + HEIGHT / HALF), ZERO), HEIGHT)
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
