from __future__ import annotations

import random
from typing import TYPE_CHECKING

# Used for type-hinting
if TYPE_CHECKING:
    from plexapi.server import PlexServer


class PlexData:
    def __init__(self, plex_server: PlexServer) -> None:
        self.plex_server = plex_server
        self.movie_sections = []
        self.show_sections = []
        self.music_sections = []
        for section in plex_server.library.sections():
            if section.type == "movie":
                self.movie_sections.append(section.title)
            if section.type == "show":
                self.show_sections.append(section.title)
            if section.type == "artist":
                self.music_sections.append(section.title)

    @property
    def movies(self) -> list:
        movies = []
        for section in self.movie_sections:
            movies.append(section.all())
        return movies

    @property
    def shoes(self) -> list:
        shows = []
        for section in self.show_sections:
            shows.append(section.all())
        return shows

    @property
    def music(self) -> list:
        music = []
        for section in self.music_sections:
            music.append(section.all())
        return music


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
