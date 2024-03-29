import time
import pygame
from server import statistics;

from peripheral.constants import (
    INITIALIZATION_ERROR,
    POINTER_REFRESH_TIME,
    READING_ERROR,
    RED,
    SCREEN_FILL,
    WHITE
)
from simulator.shoot_draw import (
    draw_mouse_pointer,
    draw_peripheral_pointer,
    draw_shoots
)
from form.form_module import form_built_flag

form_built_flag.wait()

red_points = []

async def start(screen, background_image):
    try:
        from peripheral.external_peripheral import ExternalPeripheral
        peripheral = ExternalPeripheral()
    except Exception as e:
        print(INITIALIZATION_ERROR, e)
        peripheral = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(SCREEN_FILL)
        screen.blit(background_image, (0, 0))

        if peripheral:
            try:
                pointer_position = peripheral.get_pointer_position()
                if peripheral.get_button_events():
                    red_points.append(pointer_position)
                    statistics.send_post_request(pointer_position)
            except Exception as e:
                print(READING_ERROR, e)
                peripheral = None
        else:
            pointer_position = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                red_points.append(pointer_position)
                statistics.send_post_request(pointer_position)

        if peripheral:
            draw_peripheral_pointer(pointer_position, WHITE, screen)
        else:
            draw_mouse_pointer(pointer_position, WHITE, screen)
        draw_shoots(red_points, RED, peripheral, screen)

        pygame.display.flip()
        time.sleep(POINTER_REFRESH_TIME)