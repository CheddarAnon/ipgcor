from collections import defaultdict
from typing import NamedTuple

from .gcalidx import GCalEntry, GCalIndex
from .iphotoidx import IPhotoEntry, IPhotoIndex

class Correlation(NamedTuple):
    correlated_photos: dict[GCalEntry, set[IPhotoEntry]]
    ambiguous_photos: dict[IPhotoEntry, set[GCalEntry]]
    uncorrelated: list[IPhotoEntry]

    @classmethod
    def empty():
        return Correlation(defaultdict(set), list(), defaultdict(set))


def correlate(ip: IPhotoIndex, gcal: GCalIndex):
    result = Correlation.empty()

    for p in ip.list_photos():
        events = gcal.query_for_event(p.timestamp)
        if len(events) < 1:
            result.uncorrelated += [p]
            continue
        if len(events) > 1:
            result.ambiguous_photos[p] = set(events)
            continue
        event = events[0]
        result.correlated_photos[event].add(p)

    return result
