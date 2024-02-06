import time

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


@pytest.mark.asyncio
async def test_client_credentials_instance_has_token(
    client_config, skip_if_no_client
):
    async with ClientSession() as session:
        spotify = make_spotify(session=session, **client_config)
        await spotify.auth.authorize_client()

    token = spotify.client.token
    assert token

    now = time.time()
    # token expires at is within 10 seconds of now + expires_in
    assert (
        now + token["expires_in"] - 10
        < token["expires_at"]
        < now + token["expires_in"]
    )
