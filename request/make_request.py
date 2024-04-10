import os
import aiohttp

from request.constants import (
    AUDIO,
    IMAGE,
    SCENERY
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
