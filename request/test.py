import unittest
from unittest.mock import AsyncMock, patch
from aiohttp import ClientSession, ClientResponseError

from make_request import get_image_audio

class TestMakeRequest(unittest.IsolatedAsyncioTestCase):
    async def test_get_image_audio(self):
        mocked_data = [
            {
                'image': 'https://example.com/image.jpg',
                'audio': 'https://example.com/audio.mp3'
            }
        ]

        async def mocked_request_scenery(session, scenery):
            return mocked_data

        with patch('make_request.request_scenery', new=AsyncMock(side_effect=mocked_request_scenery)):
            async with ClientSession() as session:
                image_data, audio_data = await get_image_audio('scenery')

        # Asserting the returned data
        self.assertIsNotNone(image_data)
        self.assertIsNotNone(audio_data)

    async def test_empty_response(self):
        async def mocked_request_scenery(session, scenery):
            return []

        with patch('make_request.request_scenery', new=AsyncMock(side_effect=mocked_request_scenery)):
            async with ClientSession() as session:
                with self.assertRaises(IndexError):
                    await get_image_audio('scenery')

    async def test_error_handling(self):
        async def mocked_request_scenery(session, scenery):
            raise ClientResponseError(None, None, status=500)

        with patch('make_request.request_scenery', new=AsyncMock(side_effect=mocked_request_scenery)):
            async with ClientSession() as session:
                with self.assertRaises(ClientResponseError):
                    await get_image_audio('scenery')

    async def test_invalid_data_format(self):
        async def mocked_request_scenery(session, scenery):
            return [{}]  # Missing 'image' and 'audio' keys

        with patch('make_request.request_scenery', new=AsyncMock(side_effect=mocked_request_scenery)):
            async with ClientSession() as session:
                with self.assertRaises(KeyError):
                    await get_image_audio('scenery')


if __name__ == '__main__':
    unittest.main()
