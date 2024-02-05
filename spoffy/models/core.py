from typing import List, Optional as Opt

from spoffy.models.image import Image
from spoffy.models.paging import OffsetPaging
from spoffy.models.base import SpotifyObject


class Copyright(SpotifyObject):
    text: str
    type: str


class ExternalUrls(SpotifyObject):
    spotify: str


class Restrictions(SpotifyObject):
    reason: str


class ExternalIds(SpotifyObject):
    upc: Opt[str]


class TrackExternalIds(SpotifyObject):
    isrc: str


class Followers(SpotifyObject):
    href: Opt[str]
    total: int


class ArtistSimple(SpotifyObject):
    id: str
    external_urls: ExternalUrls
    href: str
    name: str
    type: str
    uri: str


class Artist(ArtistSimple):
    followers: Followers
    genres: List[str]
    images: List[Image]
    popularity: int


class TrackLink(SpotifyObject):
    external_urls: ExternalUrls
    href: str
    id: str
    type: str
    uri: str


class TrackSimple(SpotifyObject):
    id: str
    name: str
    artists: List[ArtistSimple]
    disc_number: int
    duration_ms: int
    explicit: bool
    external_urls: ExternalUrls
    href: str
    preview_url: Opt[str]
    track_number: int
    type: str
    is_local: bool
    uri: str
    available_markets: Opt[List[str]]
    linked_from: Opt[TrackLink]
    is_playable: Opt[bool]


class AlbumBase(SpotifyObject):
    id: str
    name: str
    album_type: str
    artists: List[ArtistSimple]
    external_urls: ExternalUrls
    href: str
    images: List[Image]
    release_date: str
    release_date_precision: str
    type: str
    uri: str
    total_tracks: int


class AlbumSimple(AlbumBase):
    restrictions: Opt[Restrictions]
    available_markets: Opt[List[str]]


class Track(TrackSimple):
    album: AlbumSimple
    popularity: int
    external_ids: TrackExternalIds


class AlbumTracksPaging(OffsetPaging[TrackSimple]):
    pass


class Album(AlbumBase):
    copyrights: List[Copyright]
    external_ids: ExternalIds
    genres: List[str]
    label: str
    popularity: int
    tracks: AlbumTracksPaging
    restrictions: Opt[Restrictions]
    available_markets: Opt[List[str]]


class AlbumSimplePaging(OffsetPaging[AlbumSimple]):
    pass


class NewAlbumReleases(SpotifyObject):
    albums: AlbumSimplePaging
