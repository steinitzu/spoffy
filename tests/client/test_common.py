from collections import namedtuple

from spoffy.client.common import ClientCommon
from spoffy.models import Track


class TestPrepareRequest:
    def test__next_url__replaces_prefix(self):
        c = ClientCommon()
        c.base_url = "https://example.com"

        result = c.prepare_request(
            "GET",
            "https://api.spotify.com/v1/me/following?type=artist&limit=1",
        )

        assert (
            result.url
            == "https://example.com/me/following?type=artist&limit=1"
        )

    def test__url_no_prefix__adds_base_url(self):
        c = ClientCommon()
        url = "/me/following?type=artist"

        result = c.prepare_request("GET", url)

        assert result.url == c.base_url + url

    def test__no_token__adds_client_access_token(self):
        c = ClientCommon(access_token="sometoken")
        url = "/me"

        result = c.prepare_request("GET", url)

        assert result.headers["Authorization"] == "Bearer sometoken"


class TestLoad:
    def test__none_target__returns_none(self):
        c = ClientCommon()

        FResponse = namedtuple("Response", ["json"])  # type: ignore
        resp = FResponse(json=dict(a=1))

        assert c.load(resp, None) is None  # type:ignore

    def test__none_data__returns_none(self):
        c = ClientCommon()

        FResponse = namedtuple("Response", ["json"])  # type: ignore
        resp = FResponse(json=None)

        assert c.load(resp, Track) is None  # type:ignore
