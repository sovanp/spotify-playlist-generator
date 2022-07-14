import json

import requests

from track import Track
from playlist import Playlist

# SpotifyClient performs operations using the Spotify API
class SpotifyClient:
    def __init__(self, authorization_token, user_id):
        self.authorization_token = authorization_token
        self.user_id = user_id

    # Get the last n tracks played by a user
    def get_last_played_tracks(self, limit=10):
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["track"]["name"], track["track"]["id"], track["track"]["artists"][0]["name"]) for track in response_json["items"]]
        return tracks