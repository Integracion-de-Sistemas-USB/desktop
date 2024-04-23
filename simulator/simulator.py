from io import BytesIO
import os
import pygame
from dotenv import load_dotenv

from form.text_constants import CODE, NAME, SELECTED_PERCENTAGE, SCENERY
from peripheral.constants import (
    CAPTION,
    GENERIC_ERROR,
    SOUND_DURATION_LIMIT,
    WIDTH,
    HEIGHT,
)
from request.make_request import get_image_audio, request_stress_audio

load_dotenv()

async def play_war_sounds(data):
    pygame.mixer.init()
    stress_sound = await request_stress_audio(data['Selected Percentage'])
    war_sound = pygame.mixer.Sound(BytesIO(stress_sound))
    war_sound.play(SOUND_DURATION_LIMIT)

async def simulator(data):
    try:
        pygame.init()

        loading_font = pygame.font.SysFont('Arial', 30)
        loading_text = loading_font.render("Loading...", True, (255, 255, 255))
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        screen.fill((0, 0, 0))
        screen.blit(loading_text, (WIDTH // 2 - loading_text.get_width() // 2, HEIGHT // 2 - loading_text.get_height() // 2))
        pygame.display.flip()

        image_data, audio_data = await get_image_audio(data['Selected Option'])

        background_image = pygame.image.load(BytesIO(image_data))

        pygame.display.set_caption(CAPTION)

        if data['Selected Percentage'] != 'None':
            await play_war_sounds(data)

        pygame.mixer.init()
        background_sound = pygame.mixer.Sound(BytesIO(audio_data))
        background_sound.play(SOUND_DURATION_LIMIT)

        from calibration.calibrator import calibrate
        calibrate(screen)
        from simulator.running_loop import start
        scores = await start(screen, background_image, data[SELECTED_PERCENTAGE], data[NAME], data[CODE], data["Selected Option"])
        return scores
    
    except Exception as e:
        print(GENERIC_ERROR, e)
    finally:
        pygame.quit()
