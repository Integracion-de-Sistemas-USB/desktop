from io import BytesIO
import os
import pygame
from dotenv import load_dotenv
import aiohttp
import threading

from peripheral.constants import (
    AUDIO,
    CAPTION,
    IMAGE,
    GENERIC_ERROR,
    SOUND_DURATION_LIMIT,
    WIDTH,
    HEIGHT,
    SCENERY,
    WAR_SOUNDS
)

load_dotenv()

async def request_scenery(session, scenery):
    async with session.get(os.getenv(SCENERY) + scenery.lower()) as response:
        return await response.json()
    
async def get_image_audio(scenery):
    async with aiohttp.ClientSession() as session:
        data = await request_scenery(session, scenery)

        image_url = data[0][IMAGE]
        async with session.get(image_url) as response:
            image_data = await response.read()

        audio_url = data[0][AUDIO]
        async with session.get(audio_url) as response:
            audio_data = await response.read()

    return image_data, audio_data

def play_war_sounds():
    pygame.mixer.init()
    war_sound = pygame.mixer.Sound(os.getenv(WAR_SOUNDS))
    war_sound.play(SOUND_DURATION_LIMIT)

async def simulator(data):
    try:
        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        image_data, audio_data = await get_image_audio(data['Selected Option'])

        background_image = pygame.image.load(BytesIO(image_data))

        pygame.display.set_caption(CAPTION)

        if data['Selected Percentage'] != 'None':
            war_thread = threading.Thread(target=play_war_sounds)
            war_thread.start()

        pygame.mixer.init()
        background_sound = pygame.mixer.Sound(BytesIO(audio_data))
        background_sound.play(SOUND_DURATION_LIMIT)

        from simulator.running_loop import start
        await start(screen, background_image)
    
    except Exception as e:
        print(GENERIC_ERROR, e)
    finally:
        pygame.quit()
