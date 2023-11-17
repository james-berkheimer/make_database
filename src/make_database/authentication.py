import os

import json5 as json


class PlexAuthentication:
    """A class for handling Plex server authentication credentials.

    This class provides methods to read Plex server authentication credentials from a JSON file
    and exposes properties to access the base URL and token for authentication.

    Attributes:
        auth_file_path (str): The file path to the JSON file containing Plex server credentials.
        auth_data (dict): A dictionary containing Plex server authentication data.

    Properties:
        baseurl (str): The base URL of the Plex server.
        token (str): The authentication token for accessing the Plex server API.

    Methods:
        _resolve_auth(): Internal method to read and load Plex server authentication data from the JSON file.
    """

    def __init__(self) -> None:
        """Initialize a PlexAuthentication instance."""
        self.auth_file_path = f"{os.getenv('MEDIA_CONVEYOR')}/plex_credentials.json"
        self.auth_data = self._resolve_auth()

    def _resolve_auth(self):
        """Read and load Plex server authentication data from the JSON file."""
        with open(self.auth_file_path) as auth_file:
            return json.load(auth_file)

    @property
    def baseurl(self) -> str:
        """The base URL of the Plex server."""
        return self.auth_data["credentials"]["baseurl"]

    @property
    def token(self) -> str:
        """The authentication token for accessing the Plex server API."""
        return self.auth_data["credentials"]["token"]
