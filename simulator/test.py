import unittest
from unittest.mock import AsyncMock, patch
from aiohttp import ClientSession, ClientResponseError

from make_request import get_image_audio

class TestMakeRequest(unittest.IsolatedAsyncioTestCase):
    async def test_get_image_audio(self):
        # Mocking the data returned by the API
        mocked_data = [
            {
                'image': 'https://example.com/image.jpg',
                'audio': 'https://example.com/audio.mp3'
            }
        ]

        async def mocked_request_scenary(session, scenary):
            return mocked_data

        # Patching the request_scenary function
        with patch('make_request.request_scenary', new=AsyncMock(side_effect=mocked_request_scenary)):
            async with ClientSession() as session:
                image_data, audio_data = await get_image_audio('scenary')

        # Asserting the returned data
        self.assertIsNotNone(image_data)
        self.assertIsNotNone(audio_data)

    async def test_empty_response(self):
        async def mocked_request_scenary(session, scenary):
            return []

        with patch('make_request.request_scenary', new=AsyncMock(side_effect=mocked_request_scenary)):
            async with ClientSession() as session:
                with self.assertRaises(IndexError):
                    await get_image_audio('scenary')

    async def test_error_handling(self):
        async def mocked_request_scenary(session, scenary):
            raise ClientResponseError(None, None, status=500)

        with patch('make_request.request_scenary', new=AsyncMock(side_effect=mocked_request_scenary)):
            async with ClientSession() as session:
                with self.assertRaises(ClientResponseError):
                    await get_image_audio('scenary')

    async def test_invalid_data_format(self):
        async def mocked_request_scenary(session, scenary):
            return [{}]  # Missing 'image' and 'audio' keys

        with patch('make_request.request_scenary', new=AsyncMock(side_effect=mocked_request_scenary)):
            async with ClientSession() as session:
                with self.assertRaises(KeyError):
                    await get_image_audio('scenary')


if __name__ == '__main__':
    unittest.main()
