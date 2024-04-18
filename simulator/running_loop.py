import time
import pygame
from server.statistics import (
    send_post_request,
    send_coords_calculator
)
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
    draw_shoot,
    draw_shoots
)
from simulator.target_draw import draw_target_with_distance, calculate_score

import os

pygame.mixer.init()
shoot_sound = pygame.mixer.Sound(os.getenv(SHOOT))

red_points = []

async def start(screen, background_image, stress, name, code):
    try:
        from peripheral.external_peripheral import ExternalPeripheral
        peripheral = ExternalPeripheral()
    except Exception as e:
        print(INITIALIZATION_ERROR, e)
        peripheral = None

    start_time = time.time()
    running = True
    mouse_pressed = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(SCREEN_FILL)
        screen.blit(background_image, (0, 0))

        elapsed_time = time.time() - start_time
        timer_text = f"Time: {int(30 - elapsed_time)}s"
        timer_font = pygame.font.SysFont(None, 30)
        timer_surface = timer_font.render(timer_text, True, WHITE)
        screen.blit(timer_surface, (10, screen.get_height() - 40))

        if elapsed_time >= 30:
            running = False

        if peripheral:
            pygame.mouse.set_visible(False)
            try:
                pointer_position = peripheral.get_pointer_position()
                if peripheral.get_button_events():
                    if pointer_position != None:
                        response_data = send_coords_calculator(pointer_position, screen, stress, peripheral)
                        shoot_sound.play()
                        if calculate_score(screen, (response_data['x'], response_data['y']), stress, peripheral) > 0:
                            red_points.append((response_data['x'], response_data['y']))
                        print(f"{SCORE}:", calculate_score(screen, (response_data['x'], response_data['y']), stress, peripheral))
                        send_post_request((response_data['x'], response_data['y']), screen, name, code)
            except Exception as e:
                print(READING_ERROR, e)
                peripheral = None
        else:
            # Testing Purpose only
            pointer_position = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                if not mouse_pressed:
                    response_data = send_coords_calculator(pointer_position, screen, stress, peripheral)
                    shoot_sound.play()
                    if calculate_score(screen, (response_data['x'], response_data['y']), stress, peripheral) > 0:
                            red_points.append((response_data['x'], response_data['y']))
                    print(f"{SCORE}:", calculate_score(screen, (response_data['x'], response_data['y']), stress, peripheral))
                    send_post_request((response_data['x'], response_data['y']), screen, name, code)
                    mouse_pressed = True
            else:
                mouse_pressed = False

        draw_shoots(red_points, RED, screen, stress)
        draw_target_with_distance(stress, screen)

        pygame.display.flip()
        time.sleep(POINTER_REFRESH_TIME)
