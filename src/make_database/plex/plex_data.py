import random
from typing import TYPE_CHECKING

from plexapi.server import PlexServer

# Used for type-hinting
if TYPE_CHECKING:
    from ..authentication import PlexAuthentication


class PlexData(object):
    def __init__(self, authentication: "PlexAuthentication") -> None:
        self.baseurl = authentication.baseurl
        self.token = authentication.token

    def get_server(self):
        return PlexServer(self.baseurl, self.token)


class PlexMovies(PlexData):
    def __init__(self, authentication) -> None:
        super().__init__(authentication)
        self._movies_db = self._set_movies_db()

    def get_movies(self):
        plex = self.get_server()
        return plex.library.section("Movies").all()

    @property
    def movies_db(self):
        return self._movies_db

    def _set_movies_db(self):
        db = {}
        for movie in self.get_movies():
            db[f"movie:{random.getrandbits(32)}"] = {
                "title": movie.title,
                "year": movie.year,
                "file_path": ";".join(movie.locations),
                "thumb_path": movie.thumb,
            }
        return db
