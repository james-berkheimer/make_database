import datetime
import os
import random
import time
from pathlib import Path
from pprint import pprint

import json5 as json
from plexapi.server import PlexServer

from ..authentication import PlexAuthentication

# from .plex_data import PlexMovies

# TODO Temporarily setting the environment variable here for dev purposes
os.environ["MEDIA_CONVEYOR"] = "$HOME/.media_conveyor"


def main():
    plex_auth = PlexAuthentication()
    plex = PlexServer(plex_auth.baseurl, plex_auth.token)
    # movies = PlexMovies(plex_auth)
    # pprint(movies.movies_db)
    from collections import defaultdict

    # library_dict = defaultdict(list)
    # library_list = []
    # for section in plex.library.sections():
    #     for movie in section.all():
    #         print(movie.title)
    # print(type(plex.library.section("Movies").all()))
    # for movie in plex.library.section("Movies").all():
    #     print(type(movie))

    def get_episodes(show):
        episode_db = {}
        for season in show.seasons():
            for episode in season.episodes():
                episode_db[f"season {season.seasonNumber}"] = {
                    "episode_number": episode.episodeNumber,
                    "episode_name": episode.title,
                    "episode_location": episode.locations,
                }
        return episode_db

    for tv_show in plex.library.section("TV Shows").all():
        if tv_show.title == "Mad Men":
            # print(f"Title: {tv_show.title}\nYear: {tv_show.year}")
            # for season in tv_show.seasons():
            #     for episode in season.episodes():
            #         print(
            #             f"   S{season.seasonNumber}E{episode.episodeNumber} - {episode.title}\n{episode.locations}"
            #         )
            # print("\n")

            converted = json.dumps(get_episodes(tv_show))
            print(converted)
            print(type(converted))
            reconverted = json.loads(converted)
            print(reconverted)
            print(type(reconverted))
