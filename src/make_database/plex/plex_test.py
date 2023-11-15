import datetime
import os
import random
import time
from pathlib import Path
from pprint import pprint

from ..authentication import PlexAuthentication
from .plex_data import PlexMovies

# TODO Temporarily setting the environment variable here for dev purposes
os.environ[
    "MEDIA_CONVEYOR"
] = f"{str(Path(__file__).parent.parent.parent.parent)}/tests/configs/.plex_configs.json"


def main():
    plex_auth = PlexAuthentication()
    movies = PlexMovies(plex_auth)
    pprint(movies.movies_db)