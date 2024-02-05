from typing import Optional as Opt, List, Generic, TypeVar

from spoffy.models.base import SpotifyObject

TPageItem = TypeVar("TPageItem")


class Paging(SpotifyObject, Generic[TPageItem]):
    href: str
    limit: int
    next: Opt[str]
    previous: Opt[str]
    items: List[TPageItem]


class OffsetPaging(Paging[TPageItem]):
    """
    Offset based paging object

    :param href: Url to this object
    :param href: URL to this object
    :param limit: Max number of items per page
    :param offset: The paging offset
    :param next: URL to next page (if available)
    :param previous: URL to previous page (if available)
    """

    offset: int
    total: int


class Cursor(SpotifyObject):
    after: str
    before: str


class CursorPaging(Paging[TPageItem]):
    """
    Cursor based paging object

    :param href: URL to this object
    :param limit: Max number of items per page
    :param cursors: Cursor object for pagination
    :param next: URL to next page (if available)
    :param previous: URL to previous page (if available)
    """

    cursors: Cursor
