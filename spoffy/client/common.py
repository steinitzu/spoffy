from typing import Optional, Union, MutableMapping, Any

from spoffy.models import Token
from spoffy.sansio import Response
from spoffy.sansio import Request


class ClientCommon:
    """
    A sansio client implementation.
    This does no IO on its own.

    Args:
        access_token: A Spotify access token. Supersedes the `token` parameter
        token: A token object, either for user or client
        client_id: Client ID for oauth login
        client_secret: Client secret for oauth login
        redirect_uri: Redirect URI for oauth login
        scope: Space separated list of scopes for oauth login
        state: State string for oauth login

    """

    _default_prefix = "https://api.spotify.com/v1"

    #: Base authorize url
    authorize_url = "https://accounts.spotify.com/authorize"
    #: Token url for oauth and refresh
    token_url = "https://accounts.spotify.com/api/token"
    #: URL prefix used for all Spotify API calls
    #: This can be changed if using a proxy
    base_url = _default_prefix

    def __init__(
        self,
        access_token: Optional[str] = None,
        token: Optional[Token] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        scope: Optional[str] = None,
        state: Optional[str] = None,
    ) -> None:
        self._access_token = access_token
        self.token = token
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.state = state

    def prepare_request(
        self,
        method: str,
        url: str,
        params: Optional[MutableMapping[str, Any]] = None,
        body: Optional[Union[bytes, MutableMapping[str, Any]]] = None,
        headers: Optional[MutableMapping[str, str]] = None,
        access_token: Optional[str] = None,
    ) -> Request:
        """
        Create a request object from the given arguments

        Args:
            method: The request http method
              ( ``GET`` / ``POST`` / ``PUT`` / ``DELETE`` )
            url: The request URL, relative URLs get
              prefixed with :py:attr:`~base_url`
            params: Dict of query parameters to add to URL
            body: Request body as either bytes or json serializable dict
            headers: Dict of headers to add to request
            access_token: Override client access token
              If not provided and no explicit ``Authorization`` header,
              the :py:attr:`~access_token` stored on this instance is used
        """
        if (
            url.startswith(self._default_prefix)
            and self._default_prefix != self.base_url
        ):
            url = url.replace(self._default_prefix, self.base_url)
        elif url.startswith("http://") or url.startswith("https://"):
            pass
        else:
            url = self.base_url + url
        headers = headers or {}
        if not access_token and "Authorization" not in headers:
            access_token = self.access_token
        return Request(
            method=method,
            url=url,
            params=params,
            body=body,
            headers=headers,
            access_token=access_token,
        )

    @property
    def access_token(self) -> Union[str, None]:
        """
        Property to get the current access token
        Returns either the access_token passed to the constructor
        or the access token from this client's :py:attr:`~token` object.
        Returns ``None`` if no token
        """
        if self._access_token:
            return self._access_token
        elif self.token:
            return self.token.access_token
        return None

    @access_token.setter
    def access_token(self, access_token: str):
        self.access_token = access_token

    def load(self, response: Response, target):
        """
        Load a response data to a ``SpotifyObject`` object

        :param response: The response to load
        :param target: The target class
        """
        if target is None:
            return None
        data = response.json
        if data is None:
            return None
        return target(**data)
