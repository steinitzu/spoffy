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
    Users,
    AsyncUsers,
    Follow,
    AsyncFollow,
)


class AsyncSpotify:
    """
    Async Spotify API wrapper. Wraps the client object
    and exposes the Spotify web API organized into modules.

    Use like so:

    >>> await AsyncSpotify(...).tracks.audio_features('sometrackid')

    :ivar ~AsyncSpotify.client: The underlying client instance
    :vartype ~AsyncSpotify.client: :class:`AsyncClient`
    :ivar ~AsyncSpotify.auth: Authorization methods
    :vartype ~AsyncSpotify.auth: :py:class:`~spoffy.modules.modules.AsyncAuth`
    :ivar ~AsyncSpotify.albums: Access to album endpoints
    :vartype ~AsyncSpotify.albums: :py:class:`~spoffy.modules.modules.AsyncAlbums`
    :ivar ~AsyncSpotify.tracks: Access to track endpoints
    :vartype ~AsyncSpotify.tracks: :py:class:`~spoffy.modules.modules.AsyncTracks`
    :ivar ~AsyncSpotify.playlists: Access to playlist endpoints
    :vartype ~AsyncSpotify.playlists: :py:class:`~spoffy.modules.modules.AsyncPlaylists`
    :ivar ~AsyncSpotify.artists: Access to artist endpoints
    :vartype ~AsyncSpotify.artists: :py:class:`~spoffy.modules.modules.AsyncArtists`
    :ivar ~AsyncSpotify.search: Access to search endpoints
    :vartype ~AsyncSpotify.search: :py:class:`~spoffy.modules.modules.AsyncSearch`
    :ivar ~AsyncSpotify.player: Access to player endpoints
    :vartype ~AsyncSpotify.player: :py:class:`~spoffy.modules.modules.AsyncPlayer`
    :ivar ~AsyncSpotify.library: Access to music library endpoints
    :vartype ~AsyncSpotify.library: :py:class:`~spoffy.modules.modules.AsyncLibrary
    :ivar ~AsyncSpotify.users: Access to user endpoints
    :vartype ~AsyncSpotify.users: :py:class:`~spoffy.modules.modules.AsyncUsers
    :ivar ~AsyncSpotify.follow: Follow artists, playlists and users
    :vartype ~AsyncSpotify.follow: :py:class:`~spoffy.modules.modules.AsyncFollow


    :param client: An async client instance

    """  # noqa

    def __init__(self, client: AsyncClient) -> None:
        self.client = client

        self.artists = AsyncArtists(self.client)
        self.auth = AsyncAuth(self.client)
        self.player = AsyncPlayer(self.client)
        self.tracks = AsyncTracks(self.client)
        self.albums = AsyncAlbums(self.client)
        self.playlists = AsyncPlaylists(self.client)
        self.search = AsyncSearch(self.client)
        self.library = AsyncLibrary(self.client)
        self.users = AsyncUsers(self.client)
        self.follow = AsyncFollow(self.client)


class SyncSpotify:
    """
    Synchronous Spotify API wrapper. Wraps the client object
    and exposes the Spotify web API organized into modules.

    Use like so:

    >>> SyncSpotify(...).tracks.audio_features('sometrackid')

    :ivar ~SyncSpotify.client: The underlying client instance
    :vartype ~SyncSpotify.client: :py:class:`~SyncClient`
    :ivar ~SyncSpotify.auth: Authorization methods
    :vartype ~SyncSpotify.auth: :py:class:`~spoffy.modules.modules.Auth`
    :ivar ~SyncSpotify.albums: Access to album endpoints
    :vartype ~SyncSpotify.albums: :py:class:`~spoffy.modules.modules.Albums`
    :ivar ~SyncSpotify.tracks: Access to track endpoints
    :vartype ~SyncSpotify.tracks: :py:class:`~spoffy.modules.modules.Tracks`
    :ivar ~SyncSpotify.playlists: Access to playlist endpoints
    :vartype ~SyncSpotify.playlists: :py:class:`~spoffy.modules.modules.Playlists`
    :ivar ~SyncSpotify.artists: Access to artist endpoints
    :vartype ~SyncSpotify.artists: :py:class:`~spoffy.modules.modules.Artists`
    :ivar ~SyncSpotify.search: Access to search endpoints
    :vartype ~SyncSpotify.search: :py:class:`~spoffy.modules.modules.Search`
    :ivar ~SyncSpotify.player: Access to player endpoints
    :vartype ~SyncSpotify.player: :py:class:`~spoffy.modules.modules.Player`
    :ivar ~SyncSpotify.library: Access to music library endpoints
    :vartype ~SyncSpotify.library: :py:class:`~spoffy.modules.modules.Library`
    :ivar ~SyncSpotify.users: Access to user endpoints
    :vartype ~SyncSpotify.users: :py:class:`~spoffy.modules.modules.Users`
    :ivar ~Spotify.follow: Follow artists, playlists and users
    :vartype ~Spotify.follow: :py:class:`~spoffy.modules.modules.Follow

    :param client: An sync client instance

    """  # noqa

    def __init__(self, client: SyncClient) -> None:
        self.client = client

        self.artists = Artists(self.client)
        self.auth = Auth(self.client)
        self.player = Player(self.client)
        self.tracks = Tracks(self.client)
        self.albums = Albums(self.client)
        self.playlists = Playlists(self.client)
        self.search = Search(self.client)
        self.library = Library(self.client)
        self.users = Users(self.client)
        self.follow = Follow(self.client)
