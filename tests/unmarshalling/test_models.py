from spoffy.models import Artist, AlbumSimplePaging, Playlist, CurrentPlayback

from tests.mock.responses.get_artist import artist
from tests.mock.responses.get_artist_albums import artist_albums_relinked
from tests.mock.responses.get_playlist import (
    playlist_w_markets,
    playlist_relinked,
)
from tests.mock.responses.player import current_playback_w_track

from tests.unmarshalling.util import dict_obj_diff


def test_all():
    pairs = [
        (artist, Artist),
        (artist_albums_relinked, AlbumSimplePaging),
        (playlist_w_markets, Playlist),
        (playlist_relinked, Playlist),
        (current_playback_w_track, CurrentPlayback),
    ]

    for obj, cls in pairs:
        dict_obj_diff(obj, cls(**obj))
