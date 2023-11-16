from __future__ import annotations

import random
from typing import TYPE_CHECKING

import json5 as json

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

    def movies(self) -> list:
        movies = []
        for section in self.movie_sections:
            movies.append(section.all())
        return movies

    def shows(self) -> list:
        shows = []
        for section in self.show_sections:
            shows.append(section.all())
        return shows

    def music(self) -> list:
        music = []
        for section in self.music_sections:
            music.append(section.all())
        return music

    @property
    def movie_db(self) -> dict:
        db = {}
        for movie in self.movies():
            db[f"movie:{random.getrandbits(32)}"] = {
                "title": movie.title,
                "year": movie.year,
                "file_path": ";".join(movie.locations),
                "thumb_path": movie.thumb,
            }
        return db

    @property
    def shows_db(self) -> dict:
        show_db = {}
        for show in self.shows():
            show_db[f"show:{random.getrandbits(32)}"] = {
                "title": show.title,
                "year": show.year,
                "thumb_path": show.thumb,
                "episodes": self.get_episodes(show),
            }
        return show_db

    def get_episodes(self, show) -> str:
        episode_db = {}
        for season in show.seasons():
            for episode in season.episodes():
                episode_db[f"season {season.seasonNumber}"] = {
                    "episode_number": episode.episodeNumber,
                    "episode_name": episode.title,
                    "episode_location": episode.locations,
                }
        return json.dumps(episode_db)
