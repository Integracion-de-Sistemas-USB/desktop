from io import BytesIO
import os
import pygame
from dotenv import load_dotenv
import threading

from form.text_constants import CODE, NAME
from peripheral.constants import (
    CAPTION,
    GENERIC_ERROR,
    SOUND_DURATION_LIMIT,
    WIDTH,
    HEIGHT,
    WAR_SOUNDS
)
from request.make_request import get_image_audio

load_dotenv()

def play_war_sounds():
    pygame.mixer.init()
    war_sound = pygame.mixer.Sound(os.getenv(WAR_SOUNDS))
    war_sound.play(SOUND_DURATION_LIMIT)

async def simulator(data):
    try:
        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
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
        await start(screen, background_image, data['Selected Percentage'], data[NAME], data[CODE])
    
    except Exception as e:
        print(GENERIC_ERROR, e)
    finally:
        pygame.quit()
