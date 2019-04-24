from typing import Optional as Opt

from spoffy.models.base import SpotifyObject


class Image(SpotifyObject):
    url: str
    width: Opt[int] = None
    height: Opt[int] = None
