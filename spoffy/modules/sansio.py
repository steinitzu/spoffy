from base64 import b64encode
from typing import Sequence, Optional, Dict, Union

from spoffy.sansio import Request
from spoffy.client.common import ClientCommon
from spoffy import models


def returns(type_):
    def decorator(func):
        func.__spotify_object__ = type_
        return func

    return decorator


class RequestBuilder:
    def __init__(self, client: ClientCommon):
        self.client = client

    def b(self, *args, **kwargs):
        return self.client.prepare_request(*args, **kwargs)


class Artists(RequestBuilder):
    @returns(models.Artist)
    def artist(self, artist_id: str) -> Request:
        """
        Get an artist by Spotify ID

        :param artist_id:
        """
        return self.b(method="GET", url="/artists/{}".format(artist_id))

    @returns(models.ArtistAlbumsPaging)
    def artist_albums(
        self,
        artist_id: str,
        include_groups: Sequence[str] = None,
        market: str = None,
    ) -> Request:
        """
        Get all artist's albums

        :param artist_id:
        :param include_groups:
        :param market:
        """
        params = {}
        if include_groups:
            params["include_groups"] = ",".join(include_groups)
        if market is not None:
            params["market"] = market
        return self.b(
            method="GET",
            url="/artists/{}/albums".format(artist_id),
            params=params,
        )


class Playlists(RequestBuilder):
    @returns(models.Playlist)
    def playlist(
        self,
        playlist_id: str,
        market: Optional[str] = None,
        fields: Optional[str] = None,
    ) -> Request:
        return self.b(
            "GET",
            "/playlists/{}".format(playlist_id),
            params=_clear_nones(dict(market=market, fields=fields)),
        )

    @returns(models.PlaylistTracksPaging)
    def playlist_tracks(
        self,
        playlist_id: str,
        market: Optional[str] = None,
        fields: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Request:
        return self.b(
            "GET",
            "/playlists/{}/tracks".format(playlist_id),
            params=_clear_nones(
                dict(market=market, fields=fields, limit=limit, offset=offset)
            ),
        )


class Albums(RequestBuilder):
    """
    Interface to the Spotify albums API

    https://developer.spotify.com/documentation/web-api/reference/albums/
    """

    @returns(models.Album)
    def get_album(
        self, album_id: str, market: Optional[str] = None
    ) -> Request:
        """
        Get a single album

        :param album_id: The Spotify album ID to fetch
        :param market: ISO2A country to enable relinking
        """
        params = dict(market=market) if market is not None else None
        return self.b("GET", "/albums/{}".format(album_id), params=params)

    @returns(models.AlbumTracksPaging)
    def get_album_tracks(
        self,
        album_id: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Request:
        """
        Get tracks from the given album

        :param album_id: The Spotify album ID to fetch tracks from
        :param market: ISO2A country to enable relinking
        :param limit: Max number of results to retrieve
        :param offset: Pagination offset
        """
        params = _clear_nones(dict(market=market, limit=limit, offset=offset))
        return self.b(
            "GET", "/albums/{}/tracks".format(album_id), params=params
        )


class Tracks(RequestBuilder):
    """
    Interface to Spotify tracks API

    https://developer.spotify.com/documentation/web-api/reference/tracks
    """

    @returns(models.Track)
    def get_track(
        self, track_id: str, market: Optional[str] = None
    ) -> Request:
        """
        Get a single track

        :param track_id: The Spotify track ID to fetch
        :param market: ISO2A country to enable track relinking
        """
        params = {"market": market} if market is not None else None
        return self.b("GET", "/tracks/{}".format(track_id), params=params)

    @returns(models.TracksCollection)
    def get_many_tracks(
        self, track_ids: Sequence[str], market: Optional[str] = None
    ) -> Request:
        """
        Get several tracks by ID

        :param track_ids: List of up to 50 track IDs
        :param market: ISO2A country to enable track relinking
        """
        return self.b(
            "GET",
            "/tracks",
            params=_clear_nones(dict(ids=",".join(track_ids), market=market)),
        )

    @returns(models.AudioFeatures)
    def get_audio_features(self, track_id: str) -> Request:
        """
        Get audio features for a single track

        :param track_id: The Spotify track ID to fetch audio features for
        """
        return self.b("GET", "/audio-features/{}".format(track_id))

    @returns(models.AudioFeaturesCollection)
    def get_many_audio_features(self, track_ids: Sequence[str]) -> Request:
        """
        Get audio features for several tracks

        :param track_ids: List of up to 50 track IDs
        """
        return self.b(
            "GET", "/audio-features", params={"ids": ",".join(track_ids)}
        )


class Users(RequestBuilder):
    @returns(models.UserPublic)
    def user(self, user_id: str) -> Request:
        return self.b("GET", "/users/{}".format(user_id))

    @returns(models.UserPrivate)
    def me(self) -> Request:
        return self.b("GET", "/me")


class Player(RequestBuilder):
    @returns(None)
    def play(
        self,
        device_id: Optional[str] = None,
        context_uri: Optional[str] = None,
        uris: Optional[Sequence[str]] = None,
        offset: Optional[Dict[str, Union[str, int]]] = None,
        position_ms: Optional[int] = None,
    ) -> Request:
        """
        Play an album, track or playlist on Spotify
        """
        body = _clear_nones(
            dict(
                context_uri=context_uri,
                uris=uris,
                offset=offset,
                position_ms=position_ms,
            )
        )
        params = dict(device_id=device_id) if device_id is not None else None
        return self.b("PUT", "/me/player/play", body=body, params=params)

    @returns(models.CurrentPlayback)  # TODO: This returns None sometimes
    def current_playback(self, market: Optional[str] = None) -> Request:
        """
        Get current user's current playback status
        """
        return self.b(
            "GET", "/me/player", params=_clear_nones(dict(market=market))
        )

    @returns(None)
    def next_track(self, device_id: Optional[str] = None) -> Request:
        """
        Skip to next track in Spotify player
        """
        params = dict(device_id=device_id) if device_id is not None else None
        return self.b("PUT", "/me/player/next", params=params)

    @returns(None)
    def previous_track(self, device_id: Optional[str] = None) -> Request:
        """
        Skip to previous track in Spotify player
        """
        params = dict(device_id=device_id) if device_id is not None else None
        return self.b("PUT", "/me/player/previous", params=params)

    @returns(None)
    def pause(self, device_id: Optional[str] = None) -> Request:
        params = dict(device_id=device_id) if device_id is not None else None
        return self.b("PUT", "/me/player/pause", params=params)

    @returns(None)
    def set_volume(
        self, volume_percent: int, device_id: Optional[str] = None
    ) -> Request:
        params = _clear_nones(
            dict(device_id=device_id, volume_percent=volume_percent)
        )
        return self.b("PUT", "/me/player/volume", params=params)

    @returns(models.PlayHistoryPaging)
    def recently_played(
        self,
        limit: int = 20,
        before: Optional[int] = None,
        after: Optional[int] = None,
    ) -> Request:
        params = _clear_nones(dict(limit=limit, before=before, after=after))
        return self.b("GET", "/me/player/recently-played", params=params)


class Search(RequestBuilder):
    """
    Interface to the Spotify search API

    https://developer.spotify.com/documentation/web-api/reference/search/search/
    """

    @returns(models.SearchResults)
    def search(
        self,
        q: str,
        type: Sequence[str],
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> Request:
        params = _clear_nones(
            dict(
                q=q,
                type=",".join(type),
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            )
        )
        return self.b("GET", "/search", params=params)

    @returns(models.SearchResults)
    def artists(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> Request:
        """
        Convenience method to search for artists.
        Equivalent to `search(q, types='artist', ...)`

        :param q: The search query
        """
        return self.search(
            q=q,
            type=["artist"],
            market=market,
            limit=limit,
            offset=offset,
            include_external=include_external,
        )

    @returns(models.SearchResults)
    def albums(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> Request:
        """
        Convenience method to search for albums.
        Equivalent to `search(q, types='album', ...)`

        :param q: The search query
        """
        return self.search(
            q=q,
            type=["album"],
            market=market,
            limit=limit,
            offset=offset,
            include_external=include_external,
        )

    @returns(models.SearchResults)
    def tracks(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> Request:
        """
        Convenience method to search for tracks.
        Equivalent to `search(q, types='track', ...)`

        :param q: The search query
        """
        return self.search(
            q=q,
            type=["track"],
            market=market,
            limit=limit,
            offset=offset,
            include_external=include_external,
        )

    @returns(models.SearchResults)
    def playlists(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> Request:
        """
        Convenience method to search for playlists.
        Equivalent to `search(q, types='playlist', ...)`

        :param q: The search query
        """
        return self.search(
            q=q,
            type=["playlist"],
            market=market,
            limit=limit,
            offset=offset,
            include_external=include_external,
        )


class Library(RequestBuilder):
    """
    Manage user's saved tracks and albums

    https://developer.spotify.com/documentation/web-api/reference/library/
    """

    @returns(models.TopArtistsPaging)
    def top_artists(
        self,
        limit: Optional[int] = 20,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
    ) -> Request:
        """
        Get current user's top artists

        :param limit: Max number of results
        :param offset: Pagination offset
        :time_range: Top artists over specified time period
        """
        return self.b(
            "GET",
            "/me/top/artists",
            params=_clear_nones(
                dict(limit=limit, offset=offset, time_range=time_range)
            ),
        )

    @returns(models.TopTracksPaging)
    def top_tracks(
        self,
        limit: Optional[int] = 20,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
    ) -> Request:
        """
        Get current user's top artists

        :param limit: Max number of results
        :param offset: Pagination offset
        :time_range: Top artists over specified time period
        """
        return self.b(
            "GET",
            "/me/top/tracks",
            params=_clear_nones(
                dict(limit=limit, offset=offset, time_range=time_range)
            ),
        )

    @returns(models.SavedAlbumsPaging)
    def saved_albums(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        market: Optional[str] = None,
    ) -> Request:
        return self.b(
            "GET",
            "/me/albums",
            params=_clear_nones(
                dict(market=market, limit=limit, offset=offset)
            ),
        )

    @returns(models.SavedTracksPaging)
    def saved_tracks(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        market: Optional[str] = None,
    ) -> Request:
        return self.b(
            "GET",
            "/me/tracks",
            params=_clear_nones(
                dict(limit=limit, offset=offset, market=market)
            ),
        )

    @returns(None)
    def remove_saved_albums(self, ids: Sequence[str]) -> Request:
        return self.b("DELETE", "/me/albums", params=dict(ids=",".join(ids)))

    @returns(None)
    def add_saved_albums(self, ids: Sequence[str]) -> Request:
        return self.b("PUT", "/me/albums", params=dict(ids=",".join(ids)))

    @returns(None)
    def remove_saved_tracks(self, ids: Sequence[str]) -> Request:
        return self.b("DELETE", "/me/tracks", params=dict(ids=",".join(ids)))

    @returns(None)
    def add_saved_tracks(self, ids: Sequence[str]) -> Request:
        return self.b("PUT", "/me/tracks", params=dict(ids=",".join(ids)))


class Auth(RequestBuilder):
    @returns(models.ClientCredentialsToken)
    def get_token_from_client_credentials(self) -> Request:
        """
        Get an authorization token from client credentials
        using :py:attr:`~client.client_id` and :py:attr:`~client.client_secret`
        """
        return self.b(
            "POST",
            self.client.token_url,
            params={"grant_type": "client_credentials"},
            headers={
                "Authorization": _basic_auth_str(  # type: ignore
                    self.client.client_id, self.client.client_secret
                ),
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )

    @returns(models.UserToken)
    def get_token_from_refresh_token(
        self, refresh_token: str = None
    ) -> Request:
        """
        Get a fresh authorization token from a refresh token

        :param refresh_token: A Spotify refresh token, if `None` will
            use the refresh token stored on client instance.
        """
        if refresh_token:
            refresh = refresh_token
        elif self.client.token and self.client.token.refresh_token:
            refresh = self.client.token.refresh_token
        else:
            raise ValueError(
                "No refresh token passed and no token on instance"
            )

        return self.b(
            "POST",
            self.client.token_url,
            params=dict(refresh_token=refresh, grant_type="refresh_token"),
            headers={
                "Authorization": _basic_auth_str(  # type: ignore
                    self.client.client_id, self.client.client_secret
                ),
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )

    @returns(models.UserToken)
    def get_token_from_code(self, response_code: str, **kwargs) -> Request:
        """
        Get an authorization token from an OAuth response code

        :param response_code: The response code from redirect URL
        :param \\**kwargs: Additional keyword arguments that
           override instance attributes and are sent to the
           token API as query params
        """
        params = dict(
            redirect_uri=self.client.redirect_uri,
            code=response_code,
            grant_type="authorization_code",
            scope=self.client.scope,
            state=self.client.state,
        )
        params.update(kwargs)

        return self.b(
            "POST",
            self.client.token_url,
            params=params,
            headers={
                "Authorization": _basic_auth_str(  # type: ignore
                    self.client.client_id, self.client.client_secret
                ),
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )


def _clear_nones(params: dict):
    return {key: value for key, value in params.items() if value is not None}


def _basic_auth_str(username: str, password: str, prefix="Basic ") -> str:
    """
    Create a base64 basic auth header value from username/password
    """
    return (
        prefix
        + b64encode(b":".join((username.encode(), password.encode()))).decode()
    )
