from base64 import b64encode
from typing import Sequence, Optional, Dict, Union, Any, IO

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

    @returns(models.ArtistsCollection)
    def many_artists(self, ids: Sequence[str]) -> Request:
        """
        Get several artists by ID

        :param ids: List of Spotify artist IDs
        """
        return self.b("GET", "/artists", params=dict(ids=",".join(ids)))

    @returns(models.AlbumSimplePaging)
    def artist_albums(
        self,
        artist_id: str,
        include_groups: Sequence[str] = None,
        market: str = None,
        limit: int = None,
        offset: int = None,
    ) -> Request:
        """
        Get all artist's albums

        :param artist_id:
        :param include_groups:
        :param market:
        """
        params: Dict[str, Any] = {}
        if include_groups:
            params["include_groups"] = ",".join(include_groups)
        if market is not None:
            params["market"] = market
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        return self.b(
            method="GET",
            url="/artists/{}/albums".format(artist_id),
            params=params,
        )

    @returns(models.RelatedArtistsCollection)
    def related(self, artist_id: str) -> Request:
        """
        Get related artists for given artist_id
        """
        return self.b("GET", "/artists/{}/related-artists".format(artist_id))


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

    @returns(models.Playlist)
    def create_playlist(
        self,
        user_id: str,
        name: str,
        public: Optional[bool] = None,
        collaborative: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> Request:
        """
        Create a playlist on a user's account

        :param user_id: ID of the user account
        :param name: The playlist name
        :param public: Whether the playlist should be public
        :param collaborative: Whether the playlist should be collaborative
        :param description: Playlist description, shown in Spotify clients
        """
        return self.b(
            "POST",
            "/users/{}/playlists".format(user_id),
            body=_clear_nones(
                dict(
                    name=name,
                    public=public,
                    collaborative=collaborative,
                    description=description,
                )
            ),
        )

    @returns(models.PlaylistSnapshotId)
    def add_tracks_to_playlist(
        self,
        playlist_id: str,
        uris: Sequence[str],
        position: Optional[int] = None,
    ) -> Request:
        return self.b(
            "POST",
            "/playlists/{}/tracks".format(playlist_id),
            body=_clear_nones(dict(uris=uris, position=position)),
        )

    @returns(models.PlaylistSnapshotId)
    def remove_tracks_from_playlist(
        self,
        playlist_id: str,
        tracks: Sequence[Dict[str, Union[str, Sequence[int]]]],
        snapshot_id: Optional[str] = None,
    ) -> Request:
        """
        Remove tracks from a playlist

        :param playlist_id: Spotify ID of target playlist
        :param tracks: Iterable of dicts containing track uri
            and optionally positions.
        :param snapshot_id: Optional playlist snapshot ID to apply operation to
        """  # noqa: E501
        return self.b(
            "DELETE",
            f"/playlists/{playlist_id}/tracks",
            body=_clear_nones(dict(tracks=tracks, snapshot_id=snapshot_id)),
        )

    @returns(models.PlaylistSimplePaging)
    def my_playlists(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Request:
        return self.b(
            "GET",
            "/me/playlists",
            params=_clear_nones(dict(limit=limit, offset=offset)),
        )

    @returns(None)
    def upload_cover_image(
        self, playlist_id: str, f: Union[bytes, IO[bytes]]
    ) -> Request:
        """
        Set a new cover image for playlist

        :param f: A jpeg image file as either a file handle or a base64
             encoded bytestring
        """
        if isinstance(f, bytes):
            data = f
        else:
            data = b64encode(f.read())
        return self.b(
            "PUT",
            f"/playlists/{playlist_id}/images",
            body=data,
            headers={"Content-Type": "image/jpeg"},
        )


class Albums(RequestBuilder):
    """
    Interface to the Spotify albums API

    https://developer.spotify.com/documentation/web-api/reference/albums/
    """

    @returns(models.Album)
    def album(self, album_id: str, market: Optional[str] = None) -> Request:
        """
        Get a single album

        :param album_id: The Spotify album ID to fetch
        :param market: ISO2A country to enable relinking
        """
        params = dict(market=market) if market is not None else None
        return self.b("GET", "/albums/{}".format(album_id), params=params)

    @returns(models.AlbumTracksPaging)
    def album_tracks(
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
    def track(self, track_id: str, market: Optional[str] = None) -> Request:
        """
        Get a single track

        :param track_id: The Spotify track ID to fetch
        :param market: ISO2A country to enable track relinking
        """
        params = {"market": market} if market is not None else None
        return self.b("GET", "/tracks/{}".format(track_id), params=params)

    @returns(models.TracksCollection)
    def many_tracks(
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
    def audio_features(self, track_id: str) -> Request:
        """
        Get audio features for a single track

        :param track_id: The Spotify track ID to fetch audio features for
        """
        return self.b("GET", "/audio-features/{}".format(track_id))

    @returns(models.AudioFeaturesCollection)
    def many_audio_features(self, track_ids: Sequence[str]) -> Request:
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

    @returns(models.DevicesCollection)
    def devices(self):
        """
        Get user's available playback devices
        """
        return self.b("GET", "/me/player/devices")


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


class Follow(RequestBuilder):
    @returns(None)
    def follow_artists(self, ids: Sequence[str]) -> Request:
        return self.b(
            "PUT",
            "/me/following",
            params=dict(type="artist"),
            body=dict(ids=ids),
        )

    @returns(None)
    def follow_playlist(
        self, playlist_id: str, public: bool = None
    ) -> Request:
        return self.b(
            "PUT",
            "/playlists/{}/followers".format(playlist_id),
            body=dict(public=public) if public is not None else None,
        )

    @returns(None)
    def unfollow_playlist(self, playlist_id: str) -> Request:
        return self.b("DELETE", "/playlists/{}/followers".format(playlist_id))


class Browse(RequestBuilder):
    @returns(models.Recommendations)
    def recommendations(
        self,
        seed_artists: Optional[Sequence[str]] = None,
        seed_tracks: Optional[Sequence[str]] = None,
        seed_genres: Optional[Sequence[str]] = None,
        limit: Optional[int] = None,
        **audio_features,
    ) -> Request:
        """
        :param seed_artists: List of seed artist ids
        :param seed_tracks: List of seed track ids
        :param seed_genres: List of seed genres
        :param limit: Max number of tracks
        :param \\**audio_features: min_*/max_*/target_* audio feature filters
        """
        params: Dict[str, Any] = {}
        if seed_artists:
            params["seed_artists"] = ",".join(seed_artists)
        if seed_tracks:
            params["seed_tracks"] = ",".join(seed_tracks)
        if seed_genres:
            params["seed_genres"] = ",".join(seed_genres)
        if limit is not None:
            params["limit"] = limit
        params.update(audio_features)
        return self.b("GET", "/recommendations", params=params)

    @returns(models.NewAlbumReleases)
    def new_releases(
        self,
        country: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Request:
        return self.b(
            "GET",
            "/browse/new-releases",
            params=_clear_nones(
                dict(country=country, limit=limit, offset=offset)
            ),
        )


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
                "Authorization": _basic_auth_str(
                    self.client.client_id, self.client.client_secret  # type: ignore
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
        elif self.client.token:
            refresh = self.client.token.get("refresh_token")  # type: ignore
        if not refresh:
            raise ValueError(
                "No refresh token passed and no token on instance"
            )

        return self.b(
            "POST",
            self.client.token_url,
            params=dict(refresh_token=refresh, grant_type="refresh_token"),
            headers={
                "Authorization": _basic_auth_str(
                    self.client.client_id, self.client.client_secret  # type: ignore
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
                "Authorization": _basic_auth_str(
                    self.client.client_id, self.client.client_secret  # type: ignore
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
