from typing import List, Union

from spoffy.models.core import Track, Artist
from spoffy.models.audiofeatures import AudioFeatures
from spoffy.models.base import SpotifyObject


class TracksCollection(SpotifyObject):
    tracks: List[Union[Track, None]]


class AudioFeaturesCollection(SpotifyObject):
    audio_features: List[Union[AudioFeatures, None]]


class ArtistsCollection(SpotifyObject):
    artists: List[Union[Artist, None]]


class RelatedArtistsCollection(SpotifyObject):
    artists: List[Artist]
