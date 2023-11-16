import os

import json5 as json


class PlexAuthentication(object):
    def __init__(self) -> None:
        # TODO find a better way to handle reading in the configurations
        self.auth_file_path = os.getenv("MEDIA_CONVEYOR")
        self.auth_data = self._resolve_auth()

    def _resolve_auth(self):
        with open(self.auth_file_path) as auth_file:
            return json.load(auth_file)

    @property
    def baseurl(self):
        return self.auth_data["credentials"]["baseurl"]

    @property
    def token(self):
        return self.auth_data["credentials"]["token"]
