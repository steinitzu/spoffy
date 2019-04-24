import os

import pytest


@pytest.fixture(scope="session")
def client_config():
    return dict(
        client_id=os.getenv("SPOTIFY_TEST_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_TEST_CLIENT_SECRET"),
    )


@pytest.fixture(autouse=True)
def skip_if_no_client(client_config):
    if not client_config["client_id"]:
        pytest.skip("Skipped because no client ID set")
