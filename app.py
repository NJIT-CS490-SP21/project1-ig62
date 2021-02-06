import requests
import os
from dotenv import load_dotenv, find_dotenv
import random
from flask import Flask, render_template
from spotify import *

app = Flask(__name__)

@app.route('/')

def main():
    load_dotenv(find_dotenv())
    
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    
    random_number_a = random.randint(0, 2)
    random_number_t = random.randint(0, 9)
    
    artist_name = ["HIPPO CAMPUS", "BAD SUNS", "TWO DOOR CINEMA CLUB"]
    track_name = []
    track_id = []
    preview_url = []
    track_img = []
    
    spotify = SpotifyAPI(client_id, client_secret)
    spotify.get_access_token()                        #incorporate inside headers
    for i in range(0, 10):
        data = spotify.lookup_artist_tracks(artist_name[random_number_a])
        track_name.append(data["tracks"][i]["name"])
        track_id.append(data["tracks"][i]["id"])
        track_img.append(data["tracks"][i]["album"]["images"][1]["url"])
        track_data = spotify.lookup_tracks(track_id[i])
        preview_url.append(track_data["preview_url"])
    
    return render_template(
            "index.html",
            artist = artist_name[random_number_a],
            track_name = track_name[random_number_t],
            image = track_img[random_number_t],
            track_prev = preview_url[random_number_t]
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)