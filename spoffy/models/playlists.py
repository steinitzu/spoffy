from typing import List, Optional as Opt

from spoffy.models.image import Image
from spoffy.models.users import UserBase
from spoffy.models.core import Track, TrackLink, ExternalUrls, Followers
from spoffy.models.paging import OffsetPaging
from spoffy.models.base import SpotifyObject


class PlaylistOwner(UserBase):
    display_name: str


class PlaylistTrackAddedBy(UserBase):
    pass


class VideoThumbnail(SpotifyObject):
    url: Opt[str]


class PlaylistTrackTrack(Track):
    track: bool
    episode: bool
    available_markets: Opt[List[str]] = None
    linked_from: Opt[TrackLink] = None
    is_playable: Opt[bool] = None


class PlaylistTrack(SpotifyObject):
    added_at: Opt[str]  # todo: datetime
    added_by: Opt[PlaylistTrackAddedBy]
    is_local: bool
    primary_color: Opt[str] = None
    track: PlaylistTrackTrack
    video_thumbnail: VideoThumbnail


class PlaylistTracksPaging(OffsetPaging):
    items: List[PlaylistTrack]


class PlaylistBase(SpotifyObject):
    """
    :param collaborative:
    :param external_urls:
    :param href:
    :param id:
    :param images:
    :param name:
    :param owner:
    :param public:
    :param snapshot_id:
    :param type:
    :param uri:
    """

    collaborative: bool
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    owner: PlaylistOwner
    public: bool
    snapshot_id: str
    type: str
    uri: str


class TracksHref(SpotifyObject):
    href: str
    total: int


class PlaylistSimple(PlaylistBase):
    """
    A simplified playlist object

    :param tracks:
    """

    tracks: TracksHref


PlaylistSimple.__doc__ += PlaylistBase.__doc__  # type: ignore


class Playlist(PlaylistBase):
    """
    A complete playlist object

    :param description:
    :param followers:
    :param tracks:
    """

    description: Opt[str]
    followers: Followers
    tracks: PlaylistTracksPaging
