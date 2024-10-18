import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os
from flask import Flask, jsonify, render_template


load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

scopes = ["user-read-playback-state"]

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
    current_song = get_currently_playing()["song_title"]
    print(current_song)
    while True:
        temp_song = get_currently_playing()["song_title"]
        if temp_song != current_song:
            print(temp_song)
            current_song = temp_song

update_song()