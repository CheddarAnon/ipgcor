from collections.abc import Iterator
from datetime import datetime
from typing import NamedTuple


class IPhotoEntry(NamedTuple):
    identifier: str
    filename: str
    timestamp: datetime

class IPhotoIndex:
    def build_index():
        pass

    def list_photos() -> Iterator[IPhotoEntry]:
        """Return photos in time order."""
        pass
