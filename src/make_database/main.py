import os
import random
from pathlib import Path
from pprint import pprint

import redis

from .authentication import PlexAuthentication
from .plex.plex_data import PlexMovies

# TODO Temporarily setting the environment variable here for dev purposes
os.environ[
    "MEDIA_CONVEYOR"
] = f"{str(Path(__file__).parent.parent.parent)}/tests/configs/.plex_configs.json"

r = redis.Redis(host="localhost", port=6379, db=2, decode_responses=True)


def main():
    plex_auth = PlexAuthentication()
    movies = PlexMovies(plex_auth).movies_db

    with r.pipeline() as pipe:
        for movie_id, movie in movies.items():
            pipe.hmset(movie_id, movie)
        pipe.execute()
    r.bgsave()


def test_db():
    # print(r.keys())
    pprint(r.hgetall("movie:4037043956"))
    # pprint(r.hget)
