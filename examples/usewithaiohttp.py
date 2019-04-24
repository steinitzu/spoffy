import os
import asyncio

import aiohttp
from spoffy.io.aiohttp import make_spotify
from spoffy.models import Artist


CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]


async def get_artist(name: str) -> Artist:
    async with aiohttp.ClientSession() as session:
        spotify = make_spotify(
            session=session, client_id=CLIENT_ID, client_secret=CLIENT_SECRET
        )
        await spotify.auth.authorize_client()
        result = await spotify.search.artists("Tom Waits")
        return result.artists.items[0]


loop = asyncio.get_event_loop()

data = loop.run_until_complete(get_artist("Tom Waits"))
print("Tom waits is this popular:", data.popularity)
