import datetime
import os
import random
import time
from pathlib import Path
from pprint import pprint

from plexapi.server import PlexServer

from ..authentication import PlexAuthentication

# from .plex_data import PlexMovies

# TODO Temporarily setting the environment variable here for dev purposes
os.environ[
    "MEDIA_CONVEYOR"
] = f"{str(Path(__file__).parent.parent.parent.parent)}/tests/configs/plex_configs.json"


def main():
    plex_auth = PlexAuthentication()
    plex = PlexServer(plex_auth.baseurl, plex_auth.token)
    # movies = PlexMovies(plex_auth)
    # pprint(movies.movies_db)
    from collections import defaultdict

    library_dict = defaultdict(list)
    library_list = []
    for section in plex.library.sections():
        for movie in section.all():
            print(movie.title)

    # print(type(plex.library.section("Movies").all()))
    # for movie in plex.library.section("Movies").all():
    #     print(type(movie))
