# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_Artists_artist 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/artists/abcdefg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Artists_artist_albums 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/artists/abcdefg/albums?include_groups=a%2Cb%2Cc%2Cd%2Ce%2Cf%2Cg&market=abcdefg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Auth_get_token_from_client_credentials 1'] = "<Request(method='POST', url='https://accounts.spotify.com/api/token?grant_type=client_credentials', body=None, headers={'Authorization': 'Basic ZmFrZV9jbGllbnRfaWQ6ZmFrZV9jbGllbnRfc2VjcmV0', 'Content-Type': 'application/x-www-form-urlencoded'})>"

snapshots['test_Auth_get_token_from_code 1'] = "<Request(method='POST', url='https://accounts.spotify.com/api/token?redirect_uri&code=abcdefg&grant_type=authorization_code&scope&state', body=None, headers={'Authorization': 'Basic ZmFrZV9jbGllbnRfaWQ6ZmFrZV9jbGllbnRfc2VjcmV0', 'Content-Type': 'application/x-www-form-urlencoded'})>"

snapshots['test_Auth_get_token_from_refresh_token 1'] = "<Request(method='POST', url='https://accounts.spotify.com/api/token?refresh_token=abcdefg&grant_type=refresh_token', body=None, headers={'Authorization': 'Basic ZmFrZV9jbGllbnRfaWQ6ZmFrZV9jbGllbnRfc2VjcmV0', 'Content-Type': 'application/x-www-form-urlencoded'})>"

snapshots['test_Library_add_saved_albums 1'] = "<Request(method='PUT', url='https://api.spotify.com/v1/me/albums?ids=a%2Cb%2Cc%2Cd%2Ce%2Cf%2Cg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Library_add_saved_tracks 1'] = "<Request(method='PUT', url='https://api.spotify.com/v1/me/tracks?ids=a%2Cb%2Cc%2Cd%2Ce%2Cf%2Cg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Library_remove_saved_albums 1'] = "<Request(method='DELETE', url='https://api.spotify.com/v1/me/albums?ids=a%2Cb%2Cc%2Cd%2Ce%2Cf%2Cg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Library_remove_saved_tracks 1'] = "<Request(method='DELETE', url='https://api.spotify.com/v1/me/tracks?ids=a%2Cb%2Cc%2Cd%2Ce%2Cf%2Cg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Library_saved_albums 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/me/albums?market=stringarg&limit=50&offset=50', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Library_saved_tracks 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/me/tracks?limit=50&offset=50&market=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Player_current_playback 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/me/player?market=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Player_next_track 1'] = "<Request(method='PUT', url='https://api.spotify.com/v1/me/player/next?device_id=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Player_pause 1'] = "<Request(method='PUT', url='https://api.spotify.com/v1/me/player/pause?device_id=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Player_play 1'] = '<Request(method=\'PUT\', url=\'https://api.spotify.com/v1/me/player/play?device_id=stringarg\', body=b\'{"context_uri": "stringarg", "position_ms": 50}\', headers={\'Content-Type\': \'application/json; charset=utf-8\', \'Content-Length\': \'47\', \'Authorization\': \'Bearer fake_access_token\'})>'

snapshots['test_Player_previous_track 1'] = "<Request(method='PUT', url='https://api.spotify.com/v1/me/player/previous?device_id=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Player_recently_played 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/me/player/recently-played?limit=50&before=50&after=50', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Player_set_volume 1'] = "<Request(method='PUT', url='https://api.spotify.com/v1/me/player/volume?device_id=stringarg&volume_percent=50', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Playlists_playlist 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/playlists/abcdefg?market=stringarg&fields=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Playlists_playlist_tracks 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/playlists/abcdefg/tracks?market=stringarg&fields=stringarg&limit=50&offset=50', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Search_albums 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/search?q=abcdefg&type=album&market=stringarg&limit=50&offset=50&include_external=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Search_artists 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/search?q=abcdefg&type=artist&market=stringarg&limit=50&offset=50&include_external=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Search_playlists 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/search?q=abcdefg&type=playlist&market=stringarg&limit=50&offset=50&include_external=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Search_search 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/search?q=abcdefg&type=a%2Cb%2Cc%2Cd%2Ce%2Cf%2Cg&market=stringarg&limit=50&offset=50&include_external=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Search_tracks 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/search?q=abcdefg&type=track&market=stringarg&limit=50&offset=50&include_external=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Users_me 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/me', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Users_user 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/users/abcdefg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Library_top_artists 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/me/top/artists?limit=50&offset=50&time_range=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Library_top_tracks 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/me/top/tracks?limit=50&offset=50&time_range=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Albums_album 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/albums/abcdefg?market=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Albums_album_tracks 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/albums/abcdefg/tracks?market=stringarg&limit=50&offset=50', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Tracks_audio_features 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/audio-features/abcdefg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Tracks_many_audio_features 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/audio-features?ids=a%2Cb%2Cc%2Cd%2Ce%2Cf%2Cg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Tracks_many_tracks 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/tracks?ids=a%2Cb%2Cc%2Cd%2Ce%2Cf%2Cg&market=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Tracks_track 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/tracks/abcdefg?market=stringarg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Follow_follow_artists 1'] = '<Request(method=\'PUT\', url=\'https://api.spotify.com/v1/me/following?type=artist\', body=b\'{"ids": ["a", "b", "c", "d", "e", "f", "g"]}\', headers={\'Content-Type\': \'application/json; charset=utf-8\', \'Content-Length\': \'44\', \'Authorization\': \'Bearer fake_access_token\'})>'

snapshots['test_Follow_follow_playlist 1'] = "<Request(method='PUT', url='https://api.spotify.com/v1/playlists/abcdefg/followers', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Playlists_add_tracks_to_playlist 1'] = '<Request(method=\'POST\', url=\'https://api.spotify.com/v1/playlists/abcdefg/tracks\', body=b\'{"uris": ["a", "b", "c", "d", "e", "f", "g"], "position": 50}\', headers={\'Content-Type\': \'application/json; charset=utf-8\', \'Content-Length\': \'61\', \'Authorization\': \'Bearer fake_access_token\'})>'

snapshots['test_Playlists_create_playlist 1'] = '<Request(method=\'POST\', url=\'https://api.spotify.com/v1/users/abcdefg/playlists\', body=b\'{"name": "abcdefg", "description": "stringarg"}\', headers={\'Content-Type\': \'application/json; charset=utf-8\', \'Content-Length\': \'47\', \'Authorization\': \'Bearer fake_access_token\'})>'

snapshots['test_Browse_recommendations 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/recommendations?limit=50', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Browse_new_releases 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/browse/new-releases?country=stringarg&limit=50&offset=50', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Artists_many_artists 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/artists?ids=a%2Cb%2Cc%2Cd%2Ce%2Cf%2Cg', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"

snapshots['test_Artists_related 1'] = "<Request(method='GET', url='https://api.spotify.com/v1/artists/abcdefg/related-artists', body=None, headers={'Authorization': 'Bearer fake_access_token'})>"
