from typing import Optional, Dict, Any

from spoffy.models.base import SpotifyObject


def get_page_url(page: SpotifyObject, direction="next") -> str:
    target_keys = ["artists", "playlists", "albums", "tracks"]
    page_url: Optional[str] = page.get(direction)  # type: ignore
    if page_url:
        return page_url

    for key in target_keys:
        nested: Optional[Dict[str, Any]] = page.get(key)  # type: ignore
        if nested:
            page_url = nested.get(direction)
    if page_url:
        return page_url
    raise AttributeError(
        "{} url not found on object of type {}".format(direction, type(page))
    )
