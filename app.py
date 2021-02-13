import requests
import os
from dotenv import load_dotenv, find_dotenv
import random
from flask import Flask, render_template
from spotify import *
from genius import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 #prevents cache problem when changes in .css is done

@app.route('/')

def main():
    load_dotenv(find_dotenv()) #finds and loads informations from .env file
    
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    g_access_token = os.getenv('HACCESS_TOKEN')
    
    random_number_a = random.randint(0, 2) #random generated numbers for which artist and which track to load
    random_number_t = random.randint(0, 9)
    
    artist_name = ["ERASERHEADS", "RIVERMAYA", "PAROKYA NI EDGAR"] #hard coded list of artists
    track_name = []
    track_id = []
    preview_url = []
    track_img = []
    
    spotify = SpotifyAPI(client_id, client_secret) #initialize spotify api
    genius = GeniusAPI(g_access_token)
    spotify.get_access_token() #retrieve access token
    data = spotify.lookup_artist_tracks(artist_name[random_number_a]) #get data for artist's top tracks given the artist name at random index
    artist_img = spotify.lookup_artist_info(artist_name[random_number_a]) #get data for artist's info given the artist name at random index to retrieve artist image
    
    for i in range(0, 10): #populate track_name, track_id, preview_url, track_img using data and track_data
        track_name.append(data["tracks"][i]["name"])
        track_id.append(data["tracks"][i]["id"])
        track_img.append(data["tracks"][i]["album"]["images"][1]["url"])
        track_data = spotify.lookup_tracks(track_id[i])
        preview_url.append(track_data["preview_url"])
    
    lyrics_url = genius.get_song_info(track_name[random_number_t], artist_name[random_number_a])
    print(lyrics_url['response']['hits'][0]['result']['url'])
    return render_template(
            "index.html",
            artist = artist_name[random_number_a],
            artist_img = artist_img["images"][2]["url"],
            track_name = track_name[random_number_t],
            image = track_img[random_number_t],
            track_prev = preview_url[random_number_t],
            lyrics_url = lyrics_url['response']['hits'][0]['result']['url'],
        )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)