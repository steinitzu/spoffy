from spoffy.client.base import AsyncClient, SyncClient

from spoffy.modules.modules import (
    Auth,
    AsyncAuth,
    Artists,
    AsyncArtists,
    Player,
    AsyncPlayer,
    Tracks,
    AsyncTracks,
    Albums,
    AsyncAlbums,
    Playlists,
    AsyncPlaylists,
    Search,
    AsyncSearch,
    Library,
    AsyncLibrary,
)


class AsyncSpotify:
    """
    Async Spotify API wrapper. Wraps the client object
    and exposes the Spotify web API organized into modules.

    Use like so:

    >>> await AsyncSpotify(...).tracks.audio_features('sometrackid')

    :ivar ~Spotify.client: The underlying client instance
    :vartype ~Spotify.client: :class:`AsyncClient`
    :ivar ~Spotify.auth: Authorization methods
    :vartype ~Spotify.auth: :py:class:`~spoffy.modules.modules.AsyncAuth`
    :ivar ~Spotify.albums: Access to album endpoints
    :vartype ~Spotify.albums: :py:class:`~spoffy.modules.modules.AsyncAlbums`
    :ivar ~Spotify.tracks: Access to track endpoints
    :vartype ~Spotify.tracks: :py:class:`~spoffy.modules.modules.AsyncTracks`
    :ivar ~Spotify.playlists: Access to playlist endpoints
    :vartype ~Spotify.playlists: :py:class:`~spoffy.modules.modules.AsyncPlaylists`
    :ivar ~Spotify.artists: Access to artist endpoints
    :vartype ~Spotify.artists: :py:class:`~spoffy.modules.modules.AsyncArtists`
    :ivar ~Spotify.search: Access to search endpoints
    :vartype ~Spotify.search: :py:class:`~spoffy.modules.modules.AsyncSearch`
    :ivar ~Spotify.player: Access to player endpoints
    :vartype ~Spotify.player: :py:class:`~spoffy.modules.modules.AsyncPlayer`
    :ivar ~Spotify.library: Access to player endpoints
    :vartype ~Spotify.library: :py:class:`~spoffy.modules.modules.AsyncLibrary
    """  # noqa

    def __init__(self, client: AsyncClient) -> None:
        """
        :param client: An async client instance
        """
        self.client = client

        self.artists = AsyncArtists(self.client)
        self.auth = AsyncAuth(self.client)
        self.player = AsyncPlayer(self.client)
        self.tracks = AsyncTracks(self.client)
        self.albums = AsyncAlbums(self.client)
        self.playlists = AsyncPlaylists(self.client)
        self.search = AsyncSearch(self.client)
        self.library = AsyncLibrary(self.client)


class SyncSpotify:
    """
    Synchronous Spotify API wrapper. Wraps the client object
    and exposes the Spotify web API organized into modules.

    Use like so:

    >>> SyncSpotify(...).tracks.audio_features('sometrackid')

    :ivar ~Spotify.client: The underlying client instance
    :vartype ~Spotify.client: :py:class:`~SyncClient`
    :ivar ~Spotify.auth: Authorization methods
    :vartype ~Spotify.auth: :py:class:`~spoffy.modules.modules.Auth`
    :ivar ~Spotify.albums: Access to album endpoints
    :vartype ~Spotify.albums: :py:class:`~spoffy.modules.modules.Albums`
    :ivar ~Spotify.tracks: Access to track endpoints
    :vartype ~Spotify.tracks: :py:class:`~spoffy.modules.modules.Tracks`
    :ivar ~Spotify.playlists: Access to playlist endpoints
    :vartype ~Spotify.playlists: :py:class:`~spoffy.modules.modules.Playlists`
    :ivar ~Spotify.artists: Access to artist endpoints
    :vartype ~Spotify.artists: :py:class:`~spoffy.modules.modules.Artists`
    :ivar ~Spotify.search: Access to search endpoints
    :vartype ~Spotify.search: :py:class:`~spoffy.modules.modules.Search`
    :ivar ~Spotify.player: Access to player endpoints
    :vartype ~Spotify.player: :py:class:`~spoffy.modules.modules.Player`
    :ivar ~Spotify.library: Access to player endpoints
    :vartype ~Spotify.library: :py:class:`~spoffy.modules.modules.Library`
    """

    def __init__(self, client: SyncClient) -> None:
        """
        :param client: An sync client instance
        """
        self.client = client

        self.artists = Artists(self.client)
        self.auth = Auth(self.client)
        self.player = Player(self.client)
        self.tracks = Tracks(self.client)
        self.albums = Albums(self.client)
        self.playlists = Playlists(self.client)
        self.search = Search(self.client)
        self.library = Library(self.client)
