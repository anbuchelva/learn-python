import requests
from bs4 import BeautifulSoup
import spotify
from pprint import pprint

URL = "https://www.billboard.com/charts/hot-100/"

date_to_travel = input("Which year do you want to travel to? \nType the date in 'yyyy-mm-dd' format:\n")
# date_to_travel = "2000-01-01"
response = requests.get(url=f"{URL}{date_to_travel}")
soup = BeautifulSoup(response.text, 'lxml')
top_100_songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
songs = [song.getText().strip("\n") for song in top_100_songs]

# create_playlist(f"Billboard top 100 on {date_to_travel}")
song_uris = []
for song in songs:
    result = spotify.find_track(track=song, year=int(date_to_travel[0:4]))
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# print(song_uris)
# print(len(song_uris))

playlist_id = spotify.create_playlist(f"Billboard Top 100 {date_to_travel}")
print(playlist_id["id"])
add_tracks = spotify.add_track_to_playlist(playlist_id["id"], song_uris)
print(add_tracks)
