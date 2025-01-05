import os
from pathlib import Path
from pprint import pprint

from ..authentication import PlexAuthentication
from ..logging import setup_logger
from ..plex_data import PlexData
from ..redis_db import RedisPlexDB

logger = setup_logger()
setup_logger(level="INFO")

media_conveyor_root = Path.home() / ".media_conveyor"
project_root = Path(__file__).resolve().parent.parent.parent.parent
os.environ["MEDIA_CONVEYOR"] = str(project_root / "tests/.media_conveyor")
print(os.getenv("MEDIA_CONVEYOR"))
plex_auth = PlexAuthentication()
plex_data = PlexData(plex_auth.baseurl, plex_auth.token)


def main():
    plex_auth = PlexAuthentication()
    plex_data = PlexData(plex_auth.baseurl, plex_auth.token)
    plex_db = plex_data.compile_libraries(movies=True, db_slice=slice(100, 105))
    pprint(plex_db)
