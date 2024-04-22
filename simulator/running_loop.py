from io import BytesIO
import time
import pygame
from server.statistics import (
    send_post_request,
    send_coords_calculator
)
from request.make_request import request_shoot_audio
from peripheral.constants import (
    BULLET_LIMIT,
    INITIALIZATION_ERROR,
    POINTER_REFRESH_TIME,
    READING_ERROR,
    RED,
    SCREEN_FILL,
    STRESS_HIGH,
    STRESS_LOW,
    STRESS_MEDIUM,
    WHITE,
    SHOOT,
    SCORE
)
from simulator.shoot_draw import (
    draw_shoots,
    draw_peripheral_pointer
)
from simulator.target_draw import draw_target_with_distance, calculate_score
import aiohttp
import os

pygame.mixer.init()

red_points = []

def calculate_time(stress):
    if stress == STRESS_LOW:
        time = 30
    elif stress == STRESS_MEDIUM:
        time = 20
    elif stress == STRESS_HIGH:
        time = 10
    else:
        time = 1000
    return time

async def start(screen, background_image, stress, name, code, scenery):
    try:
        from peripheral.external_peripheral import ExternalPeripheral
        peripheral = ExternalPeripheral()
    except Exception as e:
        print(INITIALIZATION_ERROR, e)
        peripheral = None

    start_time = time.time()
    running = True
    mouse_pressed = False
    
    shoot_sound_data = await request_shoot_audio()
    
    shoot_sound = pygame.mixer.Sound(BytesIO(shoot_sound_data))

    scores = {}
    current_shoot = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(SCREEN_FILL)
        screen.blit(background_image, (0, 0))

        if stress != "None":
            stress_time = calculate_time(stress)
            elapsed_time = time.time() - start_time
            timer_text = f"Time: {int(stress_time - elapsed_time)}s"
            timer_font = pygame.font.SysFont(None, 30)
            timer_surface = timer_font.render(timer_text, True, WHITE)
            screen.blit(timer_surface, (10, screen.get_height() - 40))
        else:
            # No stress mode
            timer_text = "Time: Unlimited"
            timer_font = pygame.font.SysFont(None, 30)
            timer_surface = timer_font.render(timer_text, True, WHITE)
            screen.blit(timer_surface, (10, screen.get_height() - 40))

        # Display bullets left
        bullets_left_text = f"Bullets Left: {BULLET_LIMIT - current_shoot}"
        bullets_font = pygame.font.SysFont(None, 30)
        bullets_surface = bullets_font.render(bullets_left_text, True, WHITE)
        screen.blit(bullets_surface, (screen.get_width() - bullets_surface.get_width() - 10, screen.get_height() - 40))

        if peripheral:
            pygame.mouse.set_visible(False)
            try:
                pointer_position = peripheral.get_pointer_position()
                if peripheral.get_button_events():
                    if pointer_position != None:
                        response_data = send_coords_calculator(pointer_position, screen, stress, peripheral)
                        shoot_sound.play()
                        shoot_score = calculate_score(screen, (response_data['x'], response_data['y']), stress, peripheral)
                        scores[current_shoot] = shoot_score
                        current_shoot += 1
                        if shoot_score > 0:
                            red_points.append((response_data['x'], response_data['y']))
                        print(f"{SCORE}:", shoot_score)
                        send_post_request(name, code, scores, stress, scenery)
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
                    shoot_score = calculate_score(screen, (response_data['x'], response_data['y']), stress, peripheral)
                    scores[current_shoot] = shoot_score
                    current_shoot += 1
                    if shoot_score > 0:
                        red_points.append((response_data['x'], response_data['y']))
                    print(f"{SCORE}:", shoot_score)
                    send_post_request(name, code, scores, stress, scenery)
                    mouse_pressed = True
            else:
                mouse_pressed = False

        draw_shoots(red_points, RED, screen, stress)
        draw_target_with_distance(stress, screen)
        if stress == "None" and peripheral:
            draw_peripheral_pointer(pointer_position, RED, screen)

        pygame.display.flip()
        time.sleep(POINTER_REFRESH_TIME)

        if current_shoot == BULLET_LIMIT:
            running = False

    return scores
