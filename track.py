
#Track represents a piece of music on Spotify
class Track:
    def __init__(self, name, id, artist):
        self.name = name                                # Track name
        self.id = id                                    # Spotify track ID
        self.artist = artist                            # Track artist

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        return self.name + " by " + self.artist