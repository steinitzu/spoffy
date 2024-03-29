from spoffy.models.base import SpotifyObject


class Token(SpotifyObject):
    access_token: str
    token_type: str
    scope: str
    expires_in: int
    expires_at: int


class ClientCredentialsToken(Token):
    """
    A token generated through client credentials

    :param access_token: A Spotify access token
    :param scope: Scopes of
        this token (space seperated list)
    :param expires_in: Expiry time in seconds from token
        generation
    :param expires_at: Unix timestamp in seconds
        when this token expires
    """

    pass


class UserToken(Token):
    """
    A token generated for user through OAuth login flow

    :param access_token: A Spotify access token
    :param token_type: The token type (always `Bearer`)
    :param scope: Scopes of
        this token (space seperated list)
    :param expires_in: Expiry time in seconds from token
        generation
    :param expires_at: Unix timestamp in seconds
        when this token expires
    :param refresh_token: A Spotify refresh token
    """

    refresh_token: str
