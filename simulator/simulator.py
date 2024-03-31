from io import BytesIO
import os
import pygame
from dotenv import load_dotenv
import aiohttp

from peripheral.constants import (
    AUDIO,
    CAPTION,
    IMAGE,
    GENERIC_ERROR,
    WIDTH,
    HEIGHT,
    SCENARY,
    WAR_SOUNDS
)

load_dotenv()

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
        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        print(data)
        image_data, audio_data = await get_image_audio(data['Selected Option'])

        background_image = pygame.image.load(BytesIO(image_data))
        pygame.mixer.init()
        background_sound = pygame.mixer.Sound(BytesIO(audio_data))
        war_sound = pygame.mixer.Sound(os.getenv(WAR_SOUNDS))

        pygame.display.set_caption(CAPTION)

        background_sound.play(-1)

        if data['Selected Percentage'] != '0%':
            war_sound.play(-1)

        from simulator.running_loop import start
        await start(screen, background_image)
    
    except Exception as e:
        print(GENERIC_ERROR, e)
    finally:
        pygame.quit()
