import json

from copy import deepcopy

_jfeatures = """
{
  "audio_features": [
    {
      "danceability": 0.366,
      "energy": 0.963,
      "key": 11,
      "loudness": -5.301,
      "mode": 0,
      "speechiness": 0.142,
      "acousticness": 0.000273,
      "instrumentalness": 0.0122,
      "liveness": 0.115,
      "valence": 0.211,
      "tempo": 137.114,
      "type": "audio_features",
      "id": "7ouMYWpwJ422jRcDASZB7P",
      "uri": "spotify:track:7ouMYWpwJ422jRcDASZB7P",
      "track_href": "https://api.spotify.com/v1/tracks/7ouMYWpwJ422jRcDASZB7P",
      "analysis_url": "https://api.spotify.com/v1/audio-analysis/7ouMYWpwJ422jRcDASZB7P",
      "duration_ms": 366213,
      "time_signature": 4
    },
    {
      "danceability": 0.602,
      "energy": 0.905,
      "key": 2,
      "loudness": -4.046,
      "mode": 1,
      "speechiness": 0.0775,
      "acousticness": 0.000202,
      "instrumentalness": 0.064,
      "liveness": 0.117,
      "valence": 0.411,
      "tempo": 128.019,
      "type": "audio_features",
      "id": "4VqPOruhp5EdPBeR92t6lQ",
      "uri": "spotify:track:4VqPOruhp5EdPBeR92t6lQ",
      "track_href": "https://api.spotify.com/v1/tracks/4VqPOruhp5EdPBeR92t6lQ",
      "analysis_url": "https://api.spotify.com/v1/audio-analysis/4VqPOruhp5EdPBeR92t6lQ",
      "duration_ms": 304840,
      "time_signature": 4
    },
    {
      "danceability": 0.585,
      "energy": 0.842,
      "key": 9,
      "loudness": -5.883,
      "mode": 0,
      "speechiness": 0.0556,
      "acousticness": 0.00242,
      "instrumentalness": 0.00686,
      "liveness": 0.0866,
      "valence": 0.428,
      "tempo": 118.211,
      "type": "audio_features",
      "id": "2takcwOaAZWiXQijPHIx7B",
      "uri": "spotify:track:2takcwOaAZWiXQijPHIx7B",
      "track_href": "https://api.spotify.com/v1/tracks/2takcwOaAZWiXQijPHIx7B",
      "analysis_url": "https://api.spotify.com/v1/audio-analysis/2takcwOaAZWiXQijPHIx7B",
      "duration_ms": 237040,
      "time_signature": 4
    }
  ]
}
"""

many_audio_features = json.loads(_jfeatures)
audio_features = many_audio_features["audio_features"][0]
many_audio_features_with_null = deepcopy(many_audio_features)
many_audio_features_with_null["audio_features"].insert(1, None)
