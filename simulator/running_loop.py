import time
import pygame
from server import statistics
from peripheral.constants import (
    INITIALIZATION_ERROR,
    POINTER_REFRESH_TIME,
    READING_ERROR,
    RED,
    SCREEN_FILL,
    WHITE,
    SHOOT,
    SCORE
)
from simulator.shoot_draw import (
    draw_mouse_pointer,
    draw_peripheral_pointer,
    draw_shoots
)
from simulator.target_draw import draw_target_with_distance, calculate_score

import os

pygame.mixer.init()
shoot_sound = pygame.mixer.Sound(os.getenv(SHOOT))

red_points = []

async def start(screen, background_image, stress):
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
            if event.type == pygame.QUIT:
                running = False

        screen.fill(SCREEN_FILL)
        screen.blit(background_image, (0, 0))

        if peripheral:
            try:
                pointer_position = peripheral.get_pointer_position()
                if peripheral.get_button_events():
                    red_points.append(pointer_position)
                    shoot_sound.play()
                    print(f"{SCORE}:", calculate_score(screen, pointer_position, stress, peripheral))
                    statistics.send_post_request(pointer_position, screen)
            except Exception as e:
                print(READING_ERROR, e)
                peripheral = None
        else:
            # Testing Porpuse
            pointer_position = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if not mouse_pressed:
                    red_points.append(pointer_position)
                    shoot_sound.play()
                    print(f"{SCORE}:", calculate_score(screen, pointer_position, stress, peripheral))
                    statistics.send_post_request(pointer_position, screen)
                    mouse_pressed = True
            else:
                mouse_pressed = False

        if peripheral:
            draw_peripheral_pointer(pointer_position, WHITE, screen)
        else:
            draw_mouse_pointer(pointer_position, WHITE, screen)
        draw_shoots(red_points, RED, peripheral, screen)
        draw_target_with_distance(stress, screen)

        pygame.display.flip()
        time.sleep(POINTER_REFRESH_TIME)
