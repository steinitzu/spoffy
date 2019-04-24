import pytest
import json

from spoffy.sansio import Response
from spoffy.exceptions import (
    SpotifyException,
    SpotifyUnauthorized,
    SpotifyPremiumRequired,
)
from spoffy.modules.sansio import Library
from spoffy.client.common import ClientCommon


@pytest.fixture
def builder() -> Library:
    return Library(ClientCommon(access_token="Fake Token"))


def byte_body(d) -> bytes:
    return json.dumps(d).encode()


def test__raise_for_status__no_error(builder):
    request = builder.top_artists()
    response = Response(request, 200, {}, b"")

    response.raise_for_status()


def test__raise_for_status__401(builder):
    request = builder.top_artists()
    response = Response(request, 401, {}, b"")

    with pytest.raises(SpotifyUnauthorized):
        response.raise_for_status()


def test__raise_for_status__500(builder):
    request = builder.top_artists()
    response = Response(request, 500, {}, b"")

    with pytest.raises(SpotifyException):
        response.raise_for_status()


def test__raise_for_status__403_premium_required(builder):
    request = builder.top_artists()
    response = Response(
        request,
        403,
        {},
        byte_body(
            {
                "error": {
                    "status": 403,
                    "message": "Player command failed: Premium required",
                    "reason": "PREMIUM_REQUIRED",
                }
            }
        ),
    )

    with pytest.raises(SpotifyPremiumRequired):
        response.raise_for_status()


def test__json_when_no_content__none(builder):
    request = builder.top_artists()
    response = Response(request, 200, {}, b"")

    assert response.json is None


def test__text_when_no_content__none(builder):
    request = builder.top_artists()
    response = Response(request, 200, {}, None)

    assert response.text is None


def test__text_when_content_empty__empty_string(builder):
    request = builder.top_artists()
    response = Response(request, 200, {}, b"")

    assert response.text == ""
