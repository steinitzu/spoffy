from typing import List, Optional as Opt

from spoffy.models.core import ExternalUrls, Followers
from spoffy.models.image import Image
from spoffy.models.base import SpotifyObject


class UserBase(SpotifyObject):

    external_urls: ExternalUrls
    href: str
    id: str
    type: str
    uri: str


class UserPublic(UserBase):
    followers: Followers
    images: List[Image]
    display_name: Opt[str]


class UserPrivate(UserPublic):
    birthdate: Opt[str] = None
    country: Opt[str] = None
    email: Opt[str] = None
    product: Opt[str] = None
