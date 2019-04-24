import os
import requests

from spoffy.io.requests import make_spotify


CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]


session = requests.Session()  # Optional

spotify = make_spotify(
    session=session, client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)

spotify.auth.authorize_client()  # Client credentials auth

result = spotify.search.artists("Tom Waits")

print("Tom Waits is this popular:", result.artists.items[0].popularity)
