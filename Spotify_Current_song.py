import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os
import time
import pywinctl as pwc


load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

scopes = ["user-read-currently-playing"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri='http://localhost:5000/callback',
                                               scope=scopes))

# print(sp.current_user_playing_track())
def get_currently_playing():
    user_playing = sp.current_user_playing_track()
    if user_playing and user_playing["is_playing"]:
        song_title = user_playing["item"]["name"]
        image_url = user_playing["item"]["album"]["images"][0]["url"]
        return {"song_title": song_title, "image_url": image_url}



def update_song():
    try:
        current_song = get_currently_playing()
        print(current_song["song_title"],current_song["image_url"])
        while True:
            time.sleep(0.2)
            temp_song = pwc.getAllAppsWindowsTitles()["Spotify.exe"][0]
            if current_song["song_title"] not in temp_song:
                now_song  = get_currently_playing()
                print(now_song["song_title"],now_song["image_url"])
                current_song = now_song
    except:
        print("No Song is currently played over Spotify")

update_song()