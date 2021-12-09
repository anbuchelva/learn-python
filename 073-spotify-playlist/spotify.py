import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "<hidden>"
SPOTIFY_CLIENT_SECRET = "<hidden>"


##################
# GET AUTH TOKEN #
##################

URL = "https://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=URL,
        scope="playlist-modify-private",
        cache_path="token.txt",
        show_dialog=True,
    ))

user_id = sp.current_user()["id"]


def find_track(track, year):
    response = sp.search(q=f"track:{track} year:{year-5}-{year}", type="track", limit=10, offset=0, market="US")
    return response


def create_playlist(playlist_name):
    response = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    return response


def add_track_to_playlist(playlist_id, song_uri):
    response = sp.playlist_add_items(playlist_id=playlist_id, items=song_uri)
    return response


# create_playlist("Billboard Top 100 - test")
