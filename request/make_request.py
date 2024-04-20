import os
import aiohttp

from request.constants import (
    AUDIO,
    IMAGE,
    SCENERY,
    SHOOT,
    STRESS
)

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

async def request_shoot_audio():
    async with aiohttp.ClientSession() as session:
        async with session.get(os.getenv(SHOOT)) as response:
            data = await response.json()
            bullet_audio_url = data[0]["bullet_audio"]
            async with session.get(bullet_audio_url) as audio_response:
                audio_data = await audio_response.read()
    return audio_data

async def request_stress_audio(level):
    async with aiohttp.ClientSession() as session:
        async with session.get(os.getenv(STRESS) + level.lower()) as response:
            data = await response.json()
            stress_audio_url = data[0]["audio"]
            async with session.get(stress_audio_url) as audio_response:
                audio_data = await audio_response.read()
    return audio_data
