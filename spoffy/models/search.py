from spoffy.models.paging import OffsetPaging
from spoffy.models.core import Artist, Track, AlbumSimple
from spoffy.models.playlists import PlaylistSimple
from spoffy.models.base import SpotifyObject


class SearchArtistsPaging(OffsetPaging[Artist]):
    pass


class SearchTracksPaging(OffsetPaging[Track]):
    pass


class SearchAlbumsPaging(OffsetPaging[AlbumSimple]):
    pass


class SearchPlaylistsPaging(OffsetPaging[PlaylistSimple]):
    pass


class SearchResults(SpotifyObject):
    artists: SearchArtistsPaging
    tracks: SearchTracksPaging
    albums: SearchAlbumsPaging
    playlists: SearchPlaylistsPaging
