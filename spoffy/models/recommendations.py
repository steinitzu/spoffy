from typing import List

from spoffy.models.core import TrackSimple
from spoffy.models.base import SpotifyObject


class RecommendationSeed(SpotifyObject):
    initialPoolSize: int
    afterFilteringSize: int
    afterRelinkingSize: int
    id: str
    type: str
    href: str


class Recommendations(SpotifyObject):
    tracks: List[TrackSimple]
    seeds: List[RecommendationSeed]
