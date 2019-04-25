from typing import Sequence, Optional, Dict, Union
from spoffy import models
from spoffy.modules.apimodule import ApiModule, AsyncApiModule
from spoffy.modules import sansio as builders, mixins


class Artists(ApiModule):
    __builder_class__ = builders.Artists

    def artist(self, artist_id: str) -> models.Artist:
        """
        Get an artist by Spotify ID

        :param artist_id:
        """
        return self._make_request(
            self.b.artist(artist_id=artist_id), models.Artist
        )

    def artist_albums(
        self,
        artist_id: str,
        include_groups: Sequence[str] = None,
        market: str = None,
    ) -> models.ArtistAlbumsPaging:
        """
        Get all artist's albums

        :param artist_id:
        :param include_groups:
        :param market:
        """
        return self._make_request(
            self.b.artist_albums(
                artist_id=artist_id,
                include_groups=include_groups,
                market=market,
            ),
            models.ArtistAlbumsPaging,
        )


class AsyncArtists(AsyncApiModule):
    __builder_class__ = builders.Artists

    async def artist(self, artist_id: str) -> models.Artist:
        """
        Get an artist by Spotify ID

        :param artist_id:
        """
        return await self._make_request(
            self.b.artist(artist_id=artist_id), models.Artist
        )

    async def artist_albums(
        self,
        artist_id: str,
        include_groups: Sequence[str] = None,
        market: str = None,
    ) -> models.ArtistAlbumsPaging:
        """
        Get all artist's albums

        :param artist_id:
        :param include_groups:
        :param market:
        """
        return await self._make_request(
            self.b.artist_albums(
                artist_id=artist_id,
                include_groups=include_groups,
                market=market,
            ),
            models.ArtistAlbumsPaging,
        )


class Playlists(ApiModule):
    __builder_class__ = builders.Playlists

    def playlist(
        self,
        playlist_id: str,
        market: Optional[str] = None,
        fields: Optional[str] = None,
    ) -> models.Playlist:
        return self._make_request(
            self.b.playlist(
                playlist_id=playlist_id, market=market, fields=fields
            ),
            models.Playlist,
        )

    def playlist_tracks(
        self,
        playlist_id: str,
        market: Optional[str] = None,
        fields: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> models.PlaylistTracksPaging:
        return self._make_request(
            self.b.playlist_tracks(
                playlist_id=playlist_id,
                market=market,
                fields=fields,
                limit=limit,
                offset=offset,
            ),
            models.PlaylistTracksPaging,
        )

    def create_playlist(
        self,
        user_id: str,
        name: str,
        public: Optional[bool] = None,
        collaborative: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> models.Playlist:
        """
        Create a playlist on a user's account

        :param user_id: ID of the user account
        :param name: The playlist name
        :param public: Whether the playlist should be public
        :param collaborative: Whether the playlist should be collaborative
        :param description: Playlist description, shown in Spotify clients
        """
        return self._make_request(
            self.b.create_playlist(
                user_id=user_id,
                name=name,
                public=public,
                collaborative=collaborative,
                description=description,
            ),
            models.Playlist,
        )

    def add_tracks_to_playlist(
        self,
        playlist_id: str,
        uris: Sequence[str],
        position: Optional[int] = None,
    ) -> models.PlaylistSnapshotId:
        return self._make_request(
            self.b.add_tracks_to_playlist(
                playlist_id=playlist_id, uris=uris, position=position
            ),
            models.PlaylistSnapshotId,
        )


class AsyncPlaylists(AsyncApiModule):
    __builder_class__ = builders.Playlists

    async def playlist(
        self,
        playlist_id: str,
        market: Optional[str] = None,
        fields: Optional[str] = None,
    ) -> models.Playlist:
        return await self._make_request(
            self.b.playlist(
                playlist_id=playlist_id, market=market, fields=fields
            ),
            models.Playlist,
        )

    async def playlist_tracks(
        self,
        playlist_id: str,
        market: Optional[str] = None,
        fields: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> models.PlaylistTracksPaging:
        return await self._make_request(
            self.b.playlist_tracks(
                playlist_id=playlist_id,
                market=market,
                fields=fields,
                limit=limit,
                offset=offset,
            ),
            models.PlaylistTracksPaging,
        )

    async def create_playlist(
        self,
        user_id: str,
        name: str,
        public: Optional[bool] = None,
        collaborative: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> models.Playlist:
        """
        Create a playlist on a user's account

        :param user_id: ID of the user account
        :param name: The playlist name
        :param public: Whether the playlist should be public
        :param collaborative: Whether the playlist should be collaborative
        :param description: Playlist description, shown in Spotify clients
        """
        return await self._make_request(
            self.b.create_playlist(
                user_id=user_id,
                name=name,
                public=public,
                collaborative=collaborative,
                description=description,
            ),
            models.Playlist,
        )

    async def add_tracks_to_playlist(
        self,
        playlist_id: str,
        uris: Sequence[str],
        position: Optional[int] = None,
    ) -> models.PlaylistSnapshotId:
        return await self._make_request(
            self.b.add_tracks_to_playlist(
                playlist_id=playlist_id, uris=uris, position=position
            ),
            models.PlaylistSnapshotId,
        )


class Albums(ApiModule):
    __builder_class__ = builders.Albums

    def album(
        self, album_id: str, market: Optional[str] = None
    ) -> models.Album:
        """
        Get a single album

        :param album_id: The Spotify album ID to fetch
        :param market: ISO2A country to enable relinking
        """
        return self._make_request(
            self.b.album(album_id=album_id, market=market), models.Album
        )

    def album_tracks(
        self,
        album_id: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> models.AlbumTracksPaging:
        """
        Get tracks from the given album

        :param album_id: The Spotify album ID to fetch tracks from
        :param market: ISO2A country to enable relinking
        :param limit: Max number of results to retrieve
        :param offset: Pagination offset
        """
        return self._make_request(
            self.b.album_tracks(
                album_id=album_id, market=market, limit=limit, offset=offset
            ),
            models.AlbumTracksPaging,
        )


class AsyncAlbums(AsyncApiModule):
    __builder_class__ = builders.Albums

    async def album(
        self, album_id: str, market: Optional[str] = None
    ) -> models.Album:
        """
        Get a single album

        :param album_id: The Spotify album ID to fetch
        :param market: ISO2A country to enable relinking
        """
        return await self._make_request(
            self.b.album(album_id=album_id, market=market), models.Album
        )

    async def album_tracks(
        self,
        album_id: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> models.AlbumTracksPaging:
        """
        Get tracks from the given album

        :param album_id: The Spotify album ID to fetch tracks from
        :param market: ISO2A country to enable relinking
        :param limit: Max number of results to retrieve
        :param offset: Pagination offset
        """
        return await self._make_request(
            self.b.album_tracks(
                album_id=album_id, market=market, limit=limit, offset=offset
            ),
            models.AlbumTracksPaging,
        )


class Tracks(ApiModule):
    __builder_class__ = builders.Tracks

    def track(
        self, track_id: str, market: Optional[str] = None
    ) -> models.Track:
        """
        Get a single track

        :param track_id: The Spotify track ID to fetch
        :param market: ISO2A country to enable track relinking
        """
        return self._make_request(
            self.b.track(track_id=track_id, market=market), models.Track
        )

    def many_tracks(
        self, track_ids: Sequence[str], market: Optional[str] = None
    ) -> models.TracksCollection:
        """
        Get several tracks by ID

        :param track_ids: List of up to 50 track IDs
        :param market: ISO2A country to enable track relinking
        """
        return self._make_request(
            self.b.many_tracks(track_ids=track_ids, market=market),
            models.TracksCollection,
        )

    def audio_features(self, track_id: str) -> models.AudioFeatures:
        """
        Get audio features for a single track

        :param track_id: The Spotify track ID to fetch audio features for
        """
        return self._make_request(
            self.b.audio_features(track_id=track_id), models.AudioFeatures
        )

    def many_audio_features(
        self, track_ids: Sequence[str]
    ) -> models.AudioFeaturesCollection:
        """
        Get audio features for several tracks

        :param track_ids: List of up to 50 track IDs
        """
        return self._make_request(
            self.b.many_audio_features(track_ids=track_ids),
            models.AudioFeaturesCollection,
        )


class AsyncTracks(AsyncApiModule):
    __builder_class__ = builders.Tracks

    async def track(
        self, track_id: str, market: Optional[str] = None
    ) -> models.Track:
        """
        Get a single track

        :param track_id: The Spotify track ID to fetch
        :param market: ISO2A country to enable track relinking
        """
        return await self._make_request(
            self.b.track(track_id=track_id, market=market), models.Track
        )

    async def many_tracks(
        self, track_ids: Sequence[str], market: Optional[str] = None
    ) -> models.TracksCollection:
        """
        Get several tracks by ID

        :param track_ids: List of up to 50 track IDs
        :param market: ISO2A country to enable track relinking
        """
        return await self._make_request(
            self.b.many_tracks(track_ids=track_ids, market=market),
            models.TracksCollection,
        )

    async def audio_features(self, track_id: str) -> models.AudioFeatures:
        """
        Get audio features for a single track

        :param track_id: The Spotify track ID to fetch audio features for
        """
        return await self._make_request(
            self.b.audio_features(track_id=track_id), models.AudioFeatures
        )

    async def many_audio_features(
        self, track_ids: Sequence[str]
    ) -> models.AudioFeaturesCollection:
        """
        Get audio features for several tracks

        :param track_ids: List of up to 50 track IDs
        """
        return await self._make_request(
            self.b.many_audio_features(track_ids=track_ids),
            models.AudioFeaturesCollection,
        )


class Users(ApiModule):
    __builder_class__ = builders.Users

    def user(self, user_id: str) -> models.UserPublic:
        return self._make_request(
            self.b.user(user_id=user_id), models.UserPublic
        )

    def me(self) -> models.UserPrivate:
        return self._make_request(self.b.me(), models.UserPrivate)


class AsyncUsers(AsyncApiModule):
    __builder_class__ = builders.Users

    async def user(self, user_id: str) -> models.UserPublic:
        return await self._make_request(
            self.b.user(user_id=user_id), models.UserPublic
        )

    async def me(self) -> models.UserPrivate:
        return await self._make_request(self.b.me(), models.UserPrivate)


class Player(ApiModule):
    __builder_class__ = builders.Player

    def play(
        self,
        device_id: Optional[str] = None,
        context_uri: Optional[str] = None,
        uris: Optional[Sequence[str]] = None,
        offset: Optional[Dict[str, Union[str, int]]] = None,
        position_ms: Optional[int] = None,
    ) -> None:
        """
        Play an album, track or playlist on Spotify
        """
        return self._make_request(
            self.b.play(
                device_id=device_id,
                context_uri=context_uri,
                uris=uris,
                offset=offset,
                position_ms=position_ms,
            ),
            None,
        )

    def current_playback(
        self, market: Optional[str] = None
    ) -> models.CurrentPlayback:
        """
        Get current user's current playback status
        """
        return self._make_request(
            self.b.current_playback(market=market), models.CurrentPlayback
        )

    def next_track(self, device_id: Optional[str] = None) -> None:
        """
        Skip to next track in Spotify player
        """
        return self._make_request(self.b.next_track(device_id=device_id), None)

    def previous_track(self, device_id: Optional[str] = None) -> None:
        """
        Skip to previous track in Spotify player
        """
        return self._make_request(
            self.b.previous_track(device_id=device_id), None
        )

    def pause(self, device_id: Optional[str] = None) -> None:
        return self._make_request(self.b.pause(device_id=device_id), None)

    def set_volume(
        self, volume_percent: int, device_id: Optional[str] = None
    ) -> None:
        return self._make_request(
            self.b.set_volume(
                volume_percent=volume_percent, device_id=device_id
            ),
            None,
        )

    def recently_played(
        self,
        limit: int = 20,
        before: Optional[int] = None,
        after: Optional[int] = None,
    ) -> models.PlayHistoryPaging:
        return self._make_request(
            self.b.recently_played(limit=limit, before=before, after=after),
            models.PlayHistoryPaging,
        )


class AsyncPlayer(AsyncApiModule):
    __builder_class__ = builders.Player

    async def play(
        self,
        device_id: Optional[str] = None,
        context_uri: Optional[str] = None,
        uris: Optional[Sequence[str]] = None,
        offset: Optional[Dict[str, Union[str, int]]] = None,
        position_ms: Optional[int] = None,
    ) -> None:
        """
        Play an album, track or playlist on Spotify
        """
        return await self._make_request(
            self.b.play(
                device_id=device_id,
                context_uri=context_uri,
                uris=uris,
                offset=offset,
                position_ms=position_ms,
            ),
            None,
        )

    async def current_playback(
        self, market: Optional[str] = None
    ) -> models.CurrentPlayback:
        """
        Get current user's current playback status
        """
        return await self._make_request(
            self.b.current_playback(market=market), models.CurrentPlayback
        )

    async def next_track(self, device_id: Optional[str] = None) -> None:
        """
        Skip to next track in Spotify player
        """
        return await self._make_request(
            self.b.next_track(device_id=device_id), None
        )

    async def previous_track(self, device_id: Optional[str] = None) -> None:
        """
        Skip to previous track in Spotify player
        """
        return await self._make_request(
            self.b.previous_track(device_id=device_id), None
        )

    async def pause(self, device_id: Optional[str] = None) -> None:
        return await self._make_request(
            self.b.pause(device_id=device_id), None
        )

    async def set_volume(
        self, volume_percent: int, device_id: Optional[str] = None
    ) -> None:
        return await self._make_request(
            self.b.set_volume(
                volume_percent=volume_percent, device_id=device_id
            ),
            None,
        )

    async def recently_played(
        self,
        limit: int = 20,
        before: Optional[int] = None,
        after: Optional[int] = None,
    ) -> models.PlayHistoryPaging:
        return await self._make_request(
            self.b.recently_played(limit=limit, before=before, after=after),
            models.PlayHistoryPaging,
        )


class Search(ApiModule):
    __builder_class__ = builders.Search

    def search(
        self,
        q: str,
        type: Sequence[str],
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> models.SearchResults:
        return self._make_request(
            self.b.search(
                q=q,
                type=type,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            ),
            models.SearchResults,
        )

    def artists(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> models.SearchResults:
        """
        Convenience method to search for artists.
        Equivalent to `search(q, types='artist', ...)`

        :param q: The search query
        """
        return self._make_request(
            self.b.artists(
                q=q,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            ),
            models.SearchResults,
        )

    def albums(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> models.SearchResults:
        """
        Convenience method to search for albums.
        Equivalent to `search(q, types='album', ...)`

        :param q: The search query
        """
        return self._make_request(
            self.b.albums(
                q=q,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            ),
            models.SearchResults,
        )

    def tracks(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> models.SearchResults:
        """
        Convenience method to search for tracks.
        Equivalent to `search(q, types='track', ...)`

        :param q: The search query
        """
        return self._make_request(
            self.b.tracks(
                q=q,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            ),
            models.SearchResults,
        )

    def playlists(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> models.SearchResults:
        """
        Convenience method to search for playlists.
        Equivalent to `search(q, types='playlist', ...)`

        :param q: The search query
        """
        return self._make_request(
            self.b.playlists(
                q=q,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            ),
            models.SearchResults,
        )


class AsyncSearch(AsyncApiModule):
    __builder_class__ = builders.Search

    async def search(
        self,
        q: str,
        type: Sequence[str],
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> models.SearchResults:
        return await self._make_request(
            self.b.search(
                q=q,
                type=type,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            ),
            models.SearchResults,
        )

    async def artists(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> models.SearchResults:
        """
        Convenience method to search for artists.
        Equivalent to `search(q, types='artist', ...)`

        :param q: The search query
        """
        return await self._make_request(
            self.b.artists(
                q=q,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            ),
            models.SearchResults,
        )

    async def albums(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> models.SearchResults:
        """
        Convenience method to search for albums.
        Equivalent to `search(q, types='album', ...)`

        :param q: The search query
        """
        return await self._make_request(
            self.b.albums(
                q=q,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            ),
            models.SearchResults,
        )

    async def tracks(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> models.SearchResults:
        """
        Convenience method to search for tracks.
        Equivalent to `search(q, types='track', ...)`

        :param q: The search query
        """
        return await self._make_request(
            self.b.tracks(
                q=q,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            ),
            models.SearchResults,
        )

    async def playlists(
        self,
        q: str,
        market: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_external: Optional[str] = None,
    ) -> models.SearchResults:
        """
        Convenience method to search for playlists.
        Equivalent to `search(q, types='playlist', ...)`

        :param q: The search query
        """
        return await self._make_request(
            self.b.playlists(
                q=q,
                market=market,
                limit=limit,
                offset=offset,
                include_external=include_external,
            ),
            models.SearchResults,
        )


class Library(ApiModule):
    __builder_class__ = builders.Library

    def top_artists(
        self,
        limit: Optional[int] = 20,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
    ) -> models.TopArtistsPaging:
        """
        Get current user's top artists

        :param limit: Max number of results
        :param offset: Pagination offset
        :time_range: Top artists over specified time period
        """
        return self._make_request(
            self.b.top_artists(
                limit=limit, offset=offset, time_range=time_range
            ),
            models.TopArtistsPaging,
        )

    def top_tracks(
        self,
        limit: Optional[int] = 20,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
    ) -> models.TopTracksPaging:
        """
        Get current user's top artists

        :param limit: Max number of results
        :param offset: Pagination offset
        :time_range: Top artists over specified time period
        """
        return self._make_request(
            self.b.top_tracks(
                limit=limit, offset=offset, time_range=time_range
            ),
            models.TopTracksPaging,
        )

    def saved_albums(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        market: Optional[str] = None,
    ) -> models.SavedAlbumsPaging:
        return self._make_request(
            self.b.saved_albums(limit=limit, offset=offset, market=market),
            models.SavedAlbumsPaging,
        )

    def saved_tracks(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        market: Optional[str] = None,
    ) -> models.SavedTracksPaging:
        return self._make_request(
            self.b.saved_tracks(limit=limit, offset=offset, market=market),
            models.SavedTracksPaging,
        )

    def remove_saved_albums(self, ids: Sequence[str]) -> None:
        return self._make_request(self.b.remove_saved_albums(ids=ids), None)

    def add_saved_albums(self, ids: Sequence[str]) -> None:
        return self._make_request(self.b.add_saved_albums(ids=ids), None)

    def remove_saved_tracks(self, ids: Sequence[str]) -> None:
        return self._make_request(self.b.remove_saved_tracks(ids=ids), None)

    def add_saved_tracks(self, ids: Sequence[str]) -> None:
        return self._make_request(self.b.add_saved_tracks(ids=ids), None)


class AsyncLibrary(AsyncApiModule):
    __builder_class__ = builders.Library

    async def top_artists(
        self,
        limit: Optional[int] = 20,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
    ) -> models.TopArtistsPaging:
        """
        Get current user's top artists

        :param limit: Max number of results
        :param offset: Pagination offset
        :time_range: Top artists over specified time period
        """
        return await self._make_request(
            self.b.top_artists(
                limit=limit, offset=offset, time_range=time_range
            ),
            models.TopArtistsPaging,
        )

    async def top_tracks(
        self,
        limit: Optional[int] = 20,
        offset: Optional[int] = None,
        time_range: Optional[str] = None,
    ) -> models.TopTracksPaging:
        """
        Get current user's top artists

        :param limit: Max number of results
        :param offset: Pagination offset
        :time_range: Top artists over specified time period
        """
        return await self._make_request(
            self.b.top_tracks(
                limit=limit, offset=offset, time_range=time_range
            ),
            models.TopTracksPaging,
        )

    async def saved_albums(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        market: Optional[str] = None,
    ) -> models.SavedAlbumsPaging:
        return await self._make_request(
            self.b.saved_albums(limit=limit, offset=offset, market=market),
            models.SavedAlbumsPaging,
        )

    async def saved_tracks(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        market: Optional[str] = None,
    ) -> models.SavedTracksPaging:
        return await self._make_request(
            self.b.saved_tracks(limit=limit, offset=offset, market=market),
            models.SavedTracksPaging,
        )

    async def remove_saved_albums(self, ids: Sequence[str]) -> None:
        return await self._make_request(
            self.b.remove_saved_albums(ids=ids), None
        )

    async def add_saved_albums(self, ids: Sequence[str]) -> None:
        return await self._make_request(self.b.add_saved_albums(ids=ids), None)

    async def remove_saved_tracks(self, ids: Sequence[str]) -> None:
        return await self._make_request(
            self.b.remove_saved_tracks(ids=ids), None
        )

    async def add_saved_tracks(self, ids: Sequence[str]) -> None:
        return await self._make_request(self.b.add_saved_tracks(ids=ids), None)


class Follow(ApiModule):
    __builder_class__ = builders.Follow

    def follow_artists(self, ids: Sequence[str]) -> None:
        return self._make_request(self.b.follow_artists(ids=ids), None)

    def follow_playlist(self, playlist_id: str, public: bool = None) -> None:
        return self._make_request(
            self.b.follow_playlist(playlist_id=playlist_id, public=public),
            None,
        )


class AsyncFollow(AsyncApiModule):
    __builder_class__ = builders.Follow

    async def follow_artists(self, ids: Sequence[str]) -> None:
        return await self._make_request(self.b.follow_artists(ids=ids), None)

    async def follow_playlist(
        self, playlist_id: str, public: bool = None
    ) -> None:
        return await self._make_request(
            self.b.follow_playlist(playlist_id=playlist_id, public=public),
            None,
        )


class Auth(ApiModule, mixins.AuthMixin):
    __builder_class__ = builders.Auth

    def get_token_from_client_credentials(
        self
    ) -> models.ClientCredentialsToken:
        """
        Get an authorization token from client credentials
        using :py:attr:`~client.client_id` and :py:attr:`~client.client_secret`
        """
        return self._make_request(
            self.b.get_token_from_client_credentials(),
            models.ClientCredentialsToken,
        )

    def get_token_from_refresh_token(
        self, refresh_token: str = None
    ) -> models.UserToken:
        """
        Get a fresh authorization token from a refresh token

        :param refresh_token: A Spotify refresh token, if `None` will
            use the refresh token stored on client instance.
        """
        return self._make_request(
            self.b.get_token_from_refresh_token(refresh_token=refresh_token),
            models.UserToken,
        )

    def get_token_from_code(
        self, response_code: str, **kwargs
    ) -> models.UserToken:
        """
        Get an authorization token from an OAuth response code

        :param response_code: The response code from redirect URL
        :param \\**kwargs: Additional keyword arguments that
           override instance attributes and are sent to the
           token API as query params
        """
        return self._make_request(
            self.b.get_token_from_code(response_code=response_code, **kwargs),
            models.UserToken,
        )

    def authorize_user(self, response_code: str, **kwargs):
        """
        Authorize this API instance using a response code
        from oauth login
        """
        self._assign_result(
            "token",
            self.get_token_from_code(response_code=response_code, **kwargs),
        )

    def authorize_client(self):
        """
        Authorize this API instance using
        its client ID and client Secret
        """
        self._assign_result("token", self.get_token_from_client_credentials())

    def refresh_authorization(self, refresh_token: str = None):
        """
        :param refresh_token: Optional refresh token to use
            instead of the token stored on this instance
        """
        self._assign_result(
            "token",
            self.get_token_from_refresh_token(refresh_token=refresh_token),
        )


class AsyncAuth(AsyncApiModule, mixins.AuthMixin):
    __builder_class__ = builders.Auth

    async def get_token_from_client_credentials(
        self
    ) -> models.ClientCredentialsToken:
        """
        Get an authorization token from client credentials
        using :py:attr:`~client.client_id` and :py:attr:`~client.client_secret`
        """
        return await self._make_request(
            self.b.get_token_from_client_credentials(),
            models.ClientCredentialsToken,
        )

    async def get_token_from_refresh_token(
        self, refresh_token: str = None
    ) -> models.UserToken:
        """
        Get a fresh authorization token from a refresh token

        :param refresh_token: A Spotify refresh token, if `None` will
            use the refresh token stored on client instance.
        """
        return await self._make_request(
            self.b.get_token_from_refresh_token(refresh_token=refresh_token),
            models.UserToken,
        )

    async def get_token_from_code(
        self, response_code: str, **kwargs
    ) -> models.UserToken:
        """
        Get an authorization token from an OAuth response code

        :param response_code: The response code from redirect URL
        :param \\**kwargs: Additional keyword arguments that
           override instance attributes and are sent to the
           token API as query params
        """
        return await self._make_request(
            self.b.get_token_from_code(response_code=response_code, **kwargs),
            models.UserToken,
        )

    async def authorize_user(self, response_code: str, **kwargs):
        """
        Authorize this API instance using a response code
        from oauth login
        """
        await self._assign_result(
            "token",
            self.get_token_from_code(response_code=response_code, **kwargs),
        )

    async def authorize_client(self):
        """
        Authorize this API instance using
        its client ID and client Secret
        """
        await self._assign_result(
            "token", self.get_token_from_client_credentials()
        )

    async def refresh_authorization(self, refresh_token: str = None):
        """
        :param refresh_token: Optional refresh token to use
            instead of the token stored on this instance
        """
        await self._assign_result(
            "token",
            self.get_token_from_refresh_token(refresh_token=refresh_token),
        )
