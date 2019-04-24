from typing import Optional as Opt, List, Any

from spoffy.models.base import SpotifyObject


class Paging(SpotifyObject):
    href: str
    limit: int
    next: Opt[str]
    previous: Opt[str]
    items: List[Any]


class OffsetPaging(Paging):
    """
    Offset based paging object

    :param href: Url to this object
    :param href: URL to this object
    :param limit: Max number of items per page
    :param offset: The paging offset
    :param next: URL to next page (if available)
    :param previous: URL to previous page (if available)
    """

    # Jedi doesn't support generics, do this for now
    href: str
    limit: int
    offset: int
    total: int
    next: Opt[str]
    previous: Opt[str]


class Cursor(SpotifyObject):
    after: str
    before: str


class CursorPaging(Paging):
    """
    Cursor based paging object

    :param href: URL to this object
    :param limit: Max number of items per page
    :param cursors: Cursor object for pagination
    :param next: URL to next page (if available)
    :param previous: URL to previous page (if available)
    """

    href: str
    limit: int
    cursors: Cursor
    next: Opt[str] = None
    previous: Opt[str] = None
