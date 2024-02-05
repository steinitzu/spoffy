from spoffy.models.core import Track, Artist
from spoffy.models.paging import OffsetPaging


class TopArtistsPaging(OffsetPaging[Artist]):
    pass


class TopTracksPaging(OffsetPaging[Track]):
    pass
