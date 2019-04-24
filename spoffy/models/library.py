from typing import List

from spoffy.models.core import Track, Album
from spoffy.models.paging import OffsetPaging
from spoffy.models.base import SpotifyObject


class SavedTrack(SpotifyObject):
    added_at: str
    track: Track


class SavedTracksPaging(OffsetPaging):
    items: List[SavedTrack]


class SavedAlbum(SpotifyObject):
    added_at: str
    album: Album


class SavedAlbumsPaging(OffsetPaging):
    items: List[SavedAlbum]
