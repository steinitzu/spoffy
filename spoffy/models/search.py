from typing import List

from spoffy.models.paging import OffsetPaging
from spoffy.models.core import Artist, Track, AlbumSimple
from spoffy.models.playlists import PlaylistSimple
from spoffy.models.base import SpotifyObject


class SearchArtistsPaging(OffsetPaging):
    items: List[Artist]


class SearchTracksPaging(OffsetPaging):
    items: List[Track]


class SearchAlbumsPaging(OffsetPaging):
    items: List[AlbumSimple]


class SearchPlaylistsPaging(OffsetPaging):
    items: List[PlaylistSimple]


class SearchResults(SpotifyObject):
    artists: SearchArtistsPaging
    tracks: SearchTracksPaging
    albums: SearchAlbumsPaging
    playlists: SearchPlaylistsPaging
