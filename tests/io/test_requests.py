import pytest

from spoffy.io.requests import make_spotify


@pytest.fixture(scope="function")
def spotify_cc(client_config, skip_if_no_client):
    s = make_spotify(**client_config)
    s.auth.authorize_client()
    return s


def test__get_artist(spotify_cc):
    result = spotify_cc.artists.artist("3zunDAtRDg7kflREzWAhxl")
    assert result["name"] == "Eels"
