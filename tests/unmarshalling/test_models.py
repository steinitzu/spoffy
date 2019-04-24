from spoffy.models import Artist, ArtistAlbumsPaging

from tests.mock.responses.get_artist import artist
from tests.mock.responses.get_artist_albums import artist_albums_relinked

from tests.unmarshalling.util import dict_obj_diff


def test_all():
    pairs = [(artist, Artist), (artist_albums_relinked, ArtistAlbumsPaging)]

    for obj, cls in pairs:
        dict_obj_diff(obj, cls(**obj))
