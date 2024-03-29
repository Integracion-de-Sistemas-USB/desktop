import os
import aiohttp

from peripheral.constants import (
    AUDIO,
    IMAGE,
    SCENARY
)

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
