from io import BytesIO
import os
import pygame
from pygame.locals import QUIT
import time
from dotenv import load_dotenv
import aiohttp

from peripheral.constants import (
    AUDIO,
    CAPTION,
    IMAGE,
    INITIALIZATION_ERROR,
    SCREEN_FILL,
    READING_ERROR,
    WHITE,
    RED,
    POINTER_REFRESH_TIME,
    GENERIC_ERROR,
    WIDTH,
    HEIGHT,
    SCENARY
)

load_dotenv()

red_points = []

async def request_scenary(session, scenary):
    async with session.get(os.getenv(SCENARY) + scenary.lower()) as response:
        return await response.json()
    
async def get_image_audio(scenary):
    async with aiohttp.ClientSession() as session:
        data = await request_scenary(session, scenary)

        image_url = data[0][IMAGE]
        async with session.get(image_url) as response:
            image_data = await response.read()

        audio_url = data[0][AUDIO]
        async with session.get(audio_url) as response:
            audio_data = await response.read()

    return image_data, audio_data

async def simulator(data):
    try:
        try:
            from peripheral.external_peripheral import ExternalPeripheral
            peripheral = ExternalPeripheral()
        except Exception as e:
            print(INITIALIZATION_ERROR, e)
            peripheral = None

        from .shoot_draw import draw_mouse_pointer, draw_peripheral_pointer, draw_shoots
        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
        image_data, audio_data = await get_image_audio(data['Selected Option'])

        background_image = pygame.image.load(BytesIO(image_data))
        pygame.mixer.init()
        background_sound = pygame.mixer.Sound(BytesIO(audio_data))

        pygame.display.set_caption(CAPTION)

        background_sound.play()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            screen.fill(SCREEN_FILL)
            screen.blit(background_image, (0, 0))

            if peripheral:
                try:
                    pointer_position = peripheral.get_pointer_position()
                    if peripheral.get_button_events():
                        red_points.append(pointer_position)
                except Exception as e:
                    print(READING_ERROR, e)
                    peripheral = None
            else:
                pointer_position = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0]:
                    red_points.append(pointer_position)

            if peripheral:
                draw_peripheral_pointer(pointer_position, WHITE, screen)
            else:
                draw_mouse_pointer(pointer_position, WHITE, screen)
            draw_shoots(red_points, RED, peripheral, screen)

            pygame.display.flip()
            time.sleep(POINTER_REFRESH_TIME)
    
    except Exception as e:
        print(GENERIC_ERROR, e)
    finally:
        pygame.quit()
