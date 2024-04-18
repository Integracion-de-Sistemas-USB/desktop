import pygame
from pygame.locals import *
import time

from peripheral.constants import (
    RED,
    WHITE,
    SHOOT_ACTION,
    PRESS_STATUS,
    POINTER_REFRESH_TIME,
    INITIALIZATION_ERROR
)
from simulator.shoot_draw import draw_peripheral_pointer
from simulator.target_draw import draw_target

pygame.init()

def calibrate(screen):
    try:
        from peripheral.external_peripheral import ExternalPeripheral
        peripheral = ExternalPeripheral()
        running = True
    except Exception as e:
        print(INITIALIZATION_ERROR, e)
        peripheral = None
        running = False

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill(WHITE)

        pointer_position = peripheral.get_pointer_position()

        for event_type, status in peripheral.get_button_events():
            if event_type == SHOOT_ACTION and status == PRESS_STATUS:
                running = False

        draw_target(10, screen, True)
        draw_peripheral_pointer(pointer_position, RED, screen)

        pygame.display.flip()
        time.sleep(POINTER_REFRESH_TIME)
