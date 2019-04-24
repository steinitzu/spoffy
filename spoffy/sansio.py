import json
from typing import MutableMapping, Union, Optional, Type, Any

from urlobject import URLObject

from spoffy.exceptions import (
    SpotifyException,
    SpotifyUnauthorized,
    SpotifyPremiumRequired,
)


class Request:
    """
    :param method: The request method (`"GET"/"POST"/"PUT"/"DELETE"`)
    :param url: The request URL (absolute or relative to client base URL)
    :param body: Optional request body, can be passed either as raw bytes
        or in dict format (in which case it will be json encoded)
    :param headers: Additional request headers
    :param access_token: Will be added to Authorization header
    """

    def __init__(
        self,
        method: str,
        url: str,
        params: Optional[MutableMapping] = None,
        body: Optional[Union[bytes, MutableMapping[str, Any]]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
        access_token: Optional[str] = None,
    ):
        self.method = method
        self.url = str(URLObject(url).add_query_params(**(params or {})))
        self.headers = dict(headers or {})
        self.body = body
        if body is not None and isinstance(body, MutableMapping):
            charset = "utf-8"
            self.body = json.dumps(body).encode(charset)
            self.headers[
                "Content-Type"
            ] = f"application/json; charset={charset}"
            self.headers["Content-Length"] = str(len(self.body))
        elif body is not None and isinstance(body, bytes):
            self.body = body
            self.headers["Content-Length"] = str(len(self.body))
        if access_token:
            self.headers["Authorization"] = "Bearer " + access_token

    def __repr__(self):
        return "<{}(method={}, url={}, body={}, headers={})>".format(
            self.__class__.__name__,
            repr(self.method),
            repr(self.url),
            repr(self.body),
            repr(self.headers),
        )

    def __str__(self):
        return "Request: {} {}".format(self.method, self.url)


class Response:
    def __init__(
        self,
        request: Request,
        status_code: int,
        headers: MutableMapping,
        content: Optional[bytes] = None,
    ):
        self.request = request
        self.status_code = status_code
        self.headers = headers
        self.content = content

    def raise_for_status(self):
        """
        Raise a :class:`~spotify.exceptions.SpotifyException`
        if response status code is an error code.
        """
        if self.status_code < 400:
            return
        kwargs = dict(
            status_code=self.status_code,
            headers=self.headers,
            request_method=self.request.method,
            request_url=self.request.url,
        )
        try:
            error_info = self.json
            if isinstance(error_info["error"], dict):
                error_info = error_info["error"]
            if "error" in error_info and "message" not in error_info:
                error_info["message"] = error_info["error"]
        except Exception:
            error_info = {"status": self.status_code, "message": self.text}
        reason = error_info.get("reason")
        exc_class: Type[SpotifyException]
        if kwargs["status_code"] == 401:
            exc_class = SpotifyUnauthorized
        elif kwargs["status_code"] == 403 and reason == "PREMIUM_REQUIRED":
            exc_class = SpotifyPremiumRequired
        else:
            exc_class = SpotifyException
        kwargs["reason"] = reason
        kwargs["error_description"] = error_info.get("error_description")
        raise exc_class(error_info["message"], **kwargs)  # type: ignore

    @property
    def json(self) -> Optional[dict]:
        if not self.content:
            return None
        return json.loads(self.content)

    @property
    def text(self) -> Optional[str]:
        if self.content is None:
            return None
        return self.content.decode()
