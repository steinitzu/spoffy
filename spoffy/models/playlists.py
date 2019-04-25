from typing import List, Optional as Opt

from spoffy.models.image import Image
from spoffy.models.users import UserBase
from spoffy.models.core import Track, TrackLink, ExternalUrls, Followers
from spoffy.models.paging import OffsetPaging
from spoffy.models.base import SpotifyObject


class PlaylistSnapshotId(SpotifyObject):
    snapshot_id: str


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
    :param collaborative: Whether playlist is collaborative
    :type collaborative: :class:`bool`
    :param external_urls: Extern urls for playlist
    :type external_urls: :class:`ExternalUrls`
    :param href: URL to this object
    :type href: :class:`str`
    :param id: Playlist ID
    :type id: :class:`str`
    :param images: Playlist images
    :type images: :class:`list[]` of :class:`Image` objects
    :param name: The playlist name
    :type name: :class:`str`
    :param owner: The playlist owner
    :type owner: :class:`PlaylistOwner`
    :param public: Whether playlist is public
    :type public: :class:`bool`
    :param snapshot_id: The playlist snapshot ID
    :type snapshot_id: :class:`str`
    :param type: The type of object ('playlist')
    :type type: :class:`str`
    :param uri: The playlist URI
    :type uri: :class:`str`
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
    """
    """

    href: str
    total: int


class PlaylistSimple(PlaylistBase):
    """
    A simplified playlist object

    :param tracks: Info to access playlist tracks
    :type tracks: :class:`TracksHref`
    """

    tracks: TracksHref


PlaylistSimple.__doc__ += PlaylistBase.__doc__  # type: ignore


class Playlist(PlaylistBase):
    """
    A complete playlist object

    :param description: Text description of playlist
    :type description: :class:`str`
    :param followers: Info about playlist followers
    :type followers: :class:`Followers`
    :param tracks: Playlist tracks paginated
    :type tracks: :class:`PlaylistTracksPaging`
    """

    description: Opt[str]
    followers: Followers
    tracks: PlaylistTracksPaging


Playlist.__doc__ += PlaylistBase.__doc__  # type: ignore
