import os
import random
from pathlib import Path
from pprint import pprint

import json5 as json
import redis
from plexapi.server import PlexServer

from .authentication import PlexAuthentication
from .plex.plex_data import PlexData
from .redis_db import RedisPlexDB

# TODO Temporarily setting the environment variable here for dev purposes
os.environ["MEDIA_CONVEYOR"] = f"{Path.home()}/.media_conveyor"

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


random.seed(444)
hats = {
    f"hat:{random.getrandbits(32)}": i
    for i in (
        {
            "color": "black",
            "price": 49.99,
            "style": "fitted",
            "quantity": 1000,
            "npurchased": 0,
        },
        {
            "color": "maroon",
            "price": 59.99,
            "style": "hipster",
            "quantity": 500,
            "npurchased": 0,
        },
        {
            "color": "green",
            "price": 99.99,
            "style": "baseball",
            "quantity": 200,
            "npurchased": 0,
        },
    )
}


movies = {
    "movie:Zoolander2:2016": {
        "title": "Zoolander 2",
        "year": 2016,
        "file_path": "/media/Movies/zoolander_2_(2016)/zoolander_2_(2016).mp4",
        "thumb_path": "/library/metadata/323670/thumb/1700677611",
    },
    "movie:Zootopia:2016": {
        "title": "Zootopia",
        "year": 2016,
        "file_path": "/media/Movies/zootopia_(2016)/zootopia_(2016).mkv",
        "thumb_path": "/library/metadata/322313/thumb/1699451899",
    },
}


def main():
    plex_auth = PlexAuthentication()
    plex_data = PlexData(plex_auth.baseurl, plex_auth.token)
    # redis_db = RedisPlexDB(plex_data.package_libraries(movies=True))
    redis_db = RedisPlexDB(plex_data.movies_db)
    # redis_db = RedisPlexDB(movies)
    # redis_db = RedisPlexDB(hats)

    redis_db.make_db()

    # plex_auth = PlexAuthentication()
    # plex_server = PlexServer(plex_auth.baseurl, plex_auth.token)
    # movies = PlexData(plex_server).movie_db

    # with r.pipeline() as pipe:
    #     for movie_id, movie in movies.items():
    #         pipe.hmset(movie_id, movie)
    #     pipe.execute()
    # r.bgsave()


def test_db():
    print(r.keys())
    # pprint(r.hgetall("movie:346317923"))
    # pprint(r.hget)
