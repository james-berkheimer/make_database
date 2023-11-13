import os
from pathlib import Path

from .authentication import PlexAuthentication
from .plex_data import PlexData

os.environ[
    "MEDIA_CONVEYOR"
] = f"{str(Path(__file__).parent.parent.parent)}/tests/configs/.plex_configs.json"


def main():
    plex_auth = PlexAuthentication()
    plex_data = PlexData(plex_auth)
    movies = plex_data.get_movies()
    for movie in movies:
        print(
            f"Title: {movie.title}\nYear: {movie.year}\nLocation: {movie.locations}\nThumb: {movie.thumb}\n"
        )
