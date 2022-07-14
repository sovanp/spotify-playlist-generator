# Playlist represents a Spotify playlist
class Playlist:
    def __init__(self, name, id):
        self.name = name                            # Playlist name
        self.id = id                                # Spotify playlist ID

    def __str__(self):
        return f"Playlist: {self.name}"