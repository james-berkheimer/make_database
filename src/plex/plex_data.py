from plexapi.server import PlexServer


class PlexData(object):
    def __init__(self, authentication) -> None:
        self.baseurl = authentication.baseurl
        self.token = authentication.token

    def get_server(self):
        return PlexServer(self.baseurl, self.token)

    def get_movies(self):
        plex = self.get_server()
        return plex.library.section("Movies").all()
