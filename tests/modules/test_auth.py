from spoffy.io.requests import make_spotify


def test_make_authorize_url():
    spotify = make_spotify(
        client_id="fake_client",
        client_secret="fake_secret",
        scope="user-read-playback-state user-modify-playback-state",
    )
    url = spotify.auth.get_authorize_url(
        redirect_uri="http://localhost:8080/callback",
        show_dialog=True,
    )

    # Check url contains correct query params
    assert "client_id=fake_client" in url
    assert "redirect_uri=http%3A%2F%2Flocalhost%3A8080%2Fcallback" in url
    assert "response_type=code" in url
    assert "scope=user-read-playback-state+user-modify-playback-state" in url
    assert "show_dialog=True" in url
