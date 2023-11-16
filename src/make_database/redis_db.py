from __future__ import annotations

from typing import TYPE_CHECKING

from redis import Redis

# Used for type-hinting
if TYPE_CHECKING:
    from make_database.plex.plex_data import PlexData


class RedisDB:
    def __init__(self: "RedisDB", plex_db: PlexData) -> None:
        self.redis = Redis(host="localhost", port=6379, db=0, decode_responses=True)
        self.plex_db = plex_db
