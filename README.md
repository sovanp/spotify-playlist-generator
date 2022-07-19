# Spotify Playlist Generator

A simple Python application that leverages the Spotify Web API to generate custom playlists using seed tracks from a user's listening history. 

## Setup

1. Clone the repo `$ git clone <repo>`

2. Create a new virtual environment `$ python3 -m venv venv` and activate it `$ source venv/bin/activate`

2. Install dependencies `$ pip3 install python-dotenv` and `$ pip3 install requests`

3. Visit https://developer.spotify.com/console/get-current-user/ to obtain ```SPOTIFY_USER_ID```

4. Visit https://developer.spotify.com/console/post-playlists/ to obtain ```SPOTIFY_AUTHORIZATION_TOKEN```

Your `.env` file should be formatted as follows:

```
SPOTIFY_AUTHORIZATION_TOKEN=
SPOTIFY_USER_ID=
```

## How to Use

1. Run the command `$ python3 createplaylist.py` and follow the console instructions
