import json

from functools import partial

from spoffy.sansio import Request


make_req = partial(Request, method="GET", url="http://example.com")


def test__params_added_to_url():
    req = make_req(params=dict(market="DE", limit=100, offset=20))

    assert req.url == "http://example.com?market=DE&limit=100&offset=20"


def test__headers_always_dict():
    req = make_req(headers=None)

    assert isinstance(req.headers, dict)


def test__dict_body__content_type():
    req = make_req(method="POST", body=dict(a=[1, 2, 3, 4]))
    assert req.headers["Content-Type"] == "application/json; charset=utf-8"


def test__dict_body__content_length():
    body = dict(a=[1, 2, 3, 4])
    req = make_req(method="POST", body=body)
    assert req.headers["Content-Length"] == str(
        len(json.dumps(body).encode("utf-8"))
    )


def test__bytes_body__content_length():
    body = b"abcdefg"
    req = make_req(method="POST", body=body)
    assert req.headers["Content-Length"] == str(len(body))


def test__access_token_added():
    req = make_req(access_token="fake_token")
    assert req.headers["Authorization"] == "Bearer fake_token"
