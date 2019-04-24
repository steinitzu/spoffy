from typing import List


from spoffy.models.core import Track, Artist
from spoffy.models.paging import OffsetPaging


class TopArtistsPaging(OffsetPaging):
    items: List[Artist]


class TopTracksPaging(OffsetPaging):
    items: List[Track]
