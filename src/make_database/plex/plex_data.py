from __future__ import annotations

import logging
import random
import re

import json5 as json
from plexapi.server import PlexServer

logger = logging.getLogger(__name__)


class PlexData(PlexServer):
    def __init__(self, baseurl=None, token=None, session=None, timeout=None):
        super().__init__(baseurl, token, session, timeout)
        self._movie_sections = []
        self._shows_sections = []
        self._music_sections = []
        self._movie_sections.extend(
            section for section in self.library.sections() if section.type == "movie"
        )
        self._shows_sections.extend(
            section for section in self.library.sections() if section.type == "show"
        )
        self._music_sections.extend(
            section for section in self.library.sections() if section.type == "artist"
        )
        logger.info("PlexData initialized successfully")

    @property
    def movies(self) -> list:
        movies = [movie for section in self._movie_sections for movie in section.all()]
        logger.info(f"Retrieved {len(movies)} movies")
        return movies

    @property
    def shows(self) -> list:
        shows = [show for section in self._shows_sections for show in section.all()]
        logger.info(f"Retrieved {len(shows)} shows")
        return shows

    @property
    def music(self) -> list:
        music = [music for section in self._music_sections for music in section.all()]
        logger.info(f"Retrieved {len(music)} music")
        return music

    @property
    def movies_db(self) -> dict:
        db = {}
        pattern = re.compile(r"[^a-zA-Z0-9]")
        for movie in self.movies:
            movie_name = pattern.sub("", movie.title).strip()
            db[f"movie:{movie_name}:{movie.year}"] = {
                "title": movie.title,
                "year": movie.year,
                "file_path": str(";".join(movie.locations)),
                "thumb_path": movie.thumb,
            }
        logger.info("Generated movies database")
        return db

    @property
    def shows_db(self) -> dict:
        shows_db = {}
        pattern = re.compile(r"[^a-zA-Z0-9]")
        for show in self.shows:
            show_name = pattern.sub("", show.title).strip()
            shows_db[f"show:{show_name}:{show.year}"] = {
                "title": show.title,
                "year": show.year,
                "thumb_path": show.thumb,
                "episodes": self._get_episodes(show),
            }
        logger.info("Generated TV shows database")
        return shows_db

    def _get_episodes(self, show) -> str:
        episode_db = {}
        for season in show.seasons():
            for episode in season.episodes():
                episode_db[f"season {season.seasonNumber}"] = {
                    "episode_number": episode.episodeNumber,
                    "episode_name": episode.title,
                    "episode_location": episode.locations,
                }
        return json.dumps(episode_db)

    @property
    def music_db(self) -> dict:
        music_db = {}
        pattern = re.compile(r"[^a-zA-Z0-9]")
        for artist in self.music:
            artist_name = pattern.sub("", artist.title).strip()
            music_db[f"artist:{artist_name}"] = {
                "artist": artist.title,
                "thumb": artist.thumb,
                "tracks": self._get_tracks(artist),
            }
        logger.info("Generated music database")
        return music_db

    def _get_tracks(self, artist) -> str:
        track_db = {}
        for album in artist.albums():
            for track in album.tracks():
                track_db[f"{album.title}:{album.year}"] = {
                    "track_number": track.trackNumber,
                    "track_name": track.title,
                    "track_location": track.locations,
                }
        return json.dumps(track_db)

    def package_libraries(self, movies=False, shows=False, music=False) -> dict:
        libraries_db = {}
        if movies:
            libraries_db["movies"] = self.movies_db
        if shows:
            libraries_db["shows"] = self.shows_db
        if music:
            libraries_db["music"] = self.music

        logger.info("Libraries packaged")
        return libraries_db
