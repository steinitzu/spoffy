import pytest
import time

from spoffy.io.requests import make_spotify


@pytest.fixture(scope="function")
def spotify_cc(client_config, skip_if_no_client):
    s = make_spotify(**client_config)
    s.auth.authorize_client()
    return s


def test__get_artist(spotify_cc):
    result = spotify_cc.artists.artist("3zunDAtRDg7kflREzWAhxl")
    assert result["name"] == "Eels"


def test_client_credentials_instance_has_token(
    client_config, skip_if_no_client
):
    spotify = make_spotify(**client_config)
    spotify.auth.authorize_client()

    token = spotify.client.token
    assert token

    now = time.time()
    # token expires at is within 10 seconds of now + expires_in
    assert (
        now + token["expires_in"] - 10
        < token["expires_at"]
        < now + token["expires_in"]
    )
