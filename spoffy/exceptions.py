from typing import Optional as Opt, Dict


class SpotifyException(Exception):
    """
    Base exception for any Spotify API errors

    :param message: The error message from the API
    :param status_code: The HTTP status code of the error response
    :param url: The URL of the failed request
    :param request_method: The HTTP method of the failed request
    :param reason: The error reason as returned from the API
        (not included on all errors)
    :param error_description: A more detailed error description as
        returned from the API (not included on all errors)
    """

    def __init__(
        self,
        message: str,
        *,
        request_method: str,
        request_url: str,
        status_code: int,
        headers: Dict[str, str],
        reason: Opt[str] = None,
        error_description: Opt[str] = None,
    ):
        self.message = message
        self.status_code = status_code
        self.headers = headers
        self.reason = reason
        self.error_description = error_description
        self.request_method = request_method
        self.request_url = request_url

    def __str__(self):
        return "{status_code}: {message} ({method} {url})".format(
            status_code=self.status_code,
            message=self.message,
            method=self.request_method,
            url=self.request_url,
        )


class SpotifyUnauthorized(SpotifyException):
    """
    Raised on authorization errors such
    as when an invalid access token is used
    """


class SpotifyPremiumRequired(SpotifyException):
    """
    Raise when attempting to call and endpoint
    which requires a premium subscription with
    a free account access token
    """
