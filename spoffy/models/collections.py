from typing import List, Union

from spoffy.models.core import Track
from spoffy.models.audiofeatures import AudioFeatures
from spoffy.models.base import SpotifyObject


class TracksCollection(SpotifyObject):
    tracks: List[Union[Track, None]]


class AudioFeaturesCollection(SpotifyObject):
    audio_features: List[Union[AudioFeatures, None]]
