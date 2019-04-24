import os

from spoffy.io.requests import make_spotify

CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]


spotify = make_spotify(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

spotify.auth.authorize_client()

# You can now make requests and access public spotify data

artist = spotify.artists.artist("64mPnRMMeudAet0E62ypkx")
print(artist.name, "sucks!")
