from typing import Optional as Opt, List, Dict

from spoffy.models.core import Track, ExternalUrls
from spoffy.models.paging import CursorPaging
from spoffy.models.base import SpotifyObject


class Device(SpotifyObject):
    id: Opt[str]
    is_active: bool
    is_private_session: bool
    is_restricted: bool
    name: str
    type: str
    volume_percent: Opt[int]


class DevicesCollection(SpotifyObject):
    devices: List[Device]


class Context(SpotifyObject):
    uri: str
    href: Opt[str]
    external_urls: Opt[ExternalUrls]
    type: str


class CurrentPlayback(SpotifyObject):
    device: Device
    repeat_state: str
    shuffle_state: bool
    context: Opt[Context]
    timestamp: int
    progress_ms: Opt[int]
    is_playing: bool
    item: Opt[Track]
    currently_playing_type: str
    actions: Dict  # Undocumented param, keep as dict


class PlayHistoryItem(SpotifyObject):
    track: Track
    played_at: str
    context: Opt[Context]


class PlayHistoryPaging(CursorPaging):
    items: List[PlayHistoryItem]
