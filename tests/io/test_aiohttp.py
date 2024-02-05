import pytest

from aiohttp import ClientSession
from spoffy.io.aiohttp import make_spotify


@pytest.fixture(scope="function")
async def spotify_cc(client_config, skip_if_no_client):
    async with ClientSession() as session:
        s = make_spotify(session=session, **client_config)
        await s.auth.authorize_client()
        yield s


@pytest.mark.asyncio
async def test__get_artist(spotify_cc):
    result = await spotify_cc.artists.artist("3zunDAtRDg7kflREzWAhxl")
    assert result["name"] == "Eels"
