from spoffy.models.base import SpotifyObject


class AudioFeatures(SpotifyObject):
    duration_ms: int
    key: int
    mode: int
    time_signature: int
    acousticness: float
    danceability: float
    energy: float
    instrumentalness: float
    liveness: float
    loudness: float
    speechiness: float
    valence: float
    tempo: float
    id: str
    uri: str
    track_href: str
    analysis_url: str
    type: str
