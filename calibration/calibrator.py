import pygame
from pygame.locals import *
import time

from peripheral.constants import (
    RED,
    WHITE,
    SHOOT_ACTION,
    PRESS_STATUS,
    POINTER_REFRESH_TIME,
    INITIALIZATION_ERROR,
    STRESS_LOW
)
from simulator.shoot_draw import draw_peripheral_pointer, draw_shoot
from simulator.target_draw import draw_target

pygame.init()

def calibrate(screen):
    try:
        from peripheral.external_peripheral import ExternalPeripheral
        peripheral = ExternalPeripheral()
    except Exception as e:
        print(INITIALIZATION_ERROR, e)
        peripheral = None

    running = True
    mouse_pressed = False
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill(WHITE)

        if peripheral:
            pygame.mouse.set_visible(False)
            pointer_position = peripheral.get_pointer_position()
            for event_type, status in peripheral.get_button_events():
                if event_type == SHOOT_ACTION and status == PRESS_STATUS:
                    running = False
        else:
            pointer_position = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if not mouse_pressed:
                    running = False

        draw_target(10, screen, True)
        if peripheral:
            draw_peripheral_pointer(pointer_position, RED, screen)
        else:
            draw_shoot(pointer_position, RED, screen, STRESS_LOW)

        pygame.display.flip()
        time.sleep(POINTER_REFRESH_TIME)
