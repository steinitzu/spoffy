import pytest

from spoffy.util import get_page_url
from spoffy.models.base import SpotifyObject


class TestGetPageUrl:
    def test__finds_next_at_root_level(self):
        obj = SpotifyObject(next="https://example.com")  # type:ignore

        assert get_page_url(obj, "next") == obj["next"]  # type:ignore

    def test__finds_next_under_artists(self):
        obj = SpotifyObject(  # type:ignore
            artists=SpotifyObject(next="https://example.com")  # type:ignore
        )

        assert (
            get_page_url(obj, "next") == obj["artists"]["next"]  # type: ignore
        )

    def test__none_found__raises_valueerror(self):
        obj = SpotifyObject(foo=SpotifyObject(id="asdasds"))  # type:ignore

        with pytest.raises(AttributeError):
            get_page_url(obj, "next")
