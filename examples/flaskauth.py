import os

from flask import Flask, url_for, redirect, request
from spoffy.io.requests import make_spotify


app = Flask(__name__)

app.config["CLIENT_ID"] = os.environ["SPOTIFY_CLIENT_ID"]
app.config["CLIENT_SECRET"] = os.environ["SPOTIFY_CLIENT_SECRET"]
app.config["SCOPE"] = "user-top-read"


def get_spotify():
    return make_spotify(
        client_id=app.config["CLIENT_ID"],
        client_secret=app.config["CLIENT_SECRET"],
        scope=app.config["SCOPE"],
        redirect_uri=url_for("spotify_callback", _external=True),
    )


@app.route("/")
def authorize_spotify():
    spotify = get_spotify()
    return redirect(spotify.auth.get_authorize_url())


@app.route("/callback")
def spotify_callback():
    spotify = get_spotify()
    response_code = request.args["code"]
    spotify.auth.authorize_user(response_code)

    top_artists = spotify.library.top_artists(
        limit=1, time_range="long_term"
    ).items

    if not top_artists:
        return "<h1>You have no top artists, go listen to more music!</h1>"

    return "<h1>Your all time top artist is: {artist.name}</h1>".format(
        artist=top_artists[0]
    )
