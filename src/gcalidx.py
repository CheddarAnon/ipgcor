from datetime import datetime
from typing import List, NamedTuple


class GCalEntry(NamedTuple):
    title: str
    token: str
    calendar: str
    start: datetime
    end: datetime

class GCalIndex:
    def build_index():
        pass

    def query_for_event(t: datetime) -> List[GCalEntry]:
        """Return events which contain the datetime."""
        pass
