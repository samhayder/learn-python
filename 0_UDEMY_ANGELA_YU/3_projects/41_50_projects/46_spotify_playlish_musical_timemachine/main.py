import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth

# YouTube Music Authentication
yt = YTMusic(r"0_UDEMY_ANGELA_YU/3_projects/41_50_projects/46_spotify_playlish_musical_timemachine/browser.json")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# bake_board_web = f"https://appbrewery.github.io/bakeboard-hot-100/{date}"

billboard_web = f"https://www.billboard.com/charts/hot-100/{date}"
# Heder for billboard api
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

response = requests.get(billboard_web, headers=header)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

song_names = [title.getText().strip() for title in soup.select(selector="#title-of-a-story")]

### #YTMusic Youtube api 
# playlists = yt.get_library_playlists()
# print(f"Found {len(playlists)} playlists in your library.")
PLAYLIST_NAME = f"{date} Billboard 100"

# Check if playlist already exists
playlist_id = None
playlists = yt.get_library_playlists(limit=100)

for p in playlists:
    if p["title"] == PLAYLIST_NAME:
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        PLAYLIST_NAME,
        f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE",
    )
    print("Playlist created.")

### #Spotify
""" spotipy_client_id = "2f4fb5a9b3a94db39c5fde56d7dc1a76"
spotipy_client_secret = "506c15d047744a879a5467e4cca244e7"
    
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://samhayder.com/spotify",
        client_id=spotipy_client_id,
        client_secret=spotipy_client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="31r5hpntbb33rvzqlr7xj2hcw56q", 
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.") """
        
### #Youtube Music Api
# Create playlist
playlist_name = f"{date} Billboard 100"
playlist_id = yt.create_playlist(
    playlist_name,
    f"Top songs from {date}",
    privacy_status="PRIVATE",
)
print(f"Created playlist: {playlist_name}")

# Search and add each song
for song in song_names:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")