from __future__ import annotations

import random
from typing import TYPE_CHECKING

# Used for type-hinting
if TYPE_CHECKING:
    from plexapi.server import PlexServer


class PlexData:
    def __init__(self, plex_server: PlexServer, sections: list = None) -> None:
        self.plex_server = plex_server
        if sections is None:
            sections = self.plex_server.library.sections()
        self.sections = sections

    @property
    def movies(self):
        return self._movies

    @movies.setter
    def movies(self, movies):
        self._movies = movies

    @property
    def shows(self):
        return self._shows

    @shows.setter
    def shows(self, shows):
        self._shows = shows

    @property
    def music(self):
        return self._music

    @music.setter
    def music(self, music):
        self._music = music


    def parse_sections(self):
        for section in self.sections:
            if section.type == "movie":



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
