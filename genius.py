import requests
import os
from dotenv import load_dotenv, find_dotenv

class GeniusAPI(object):
    access_token = None

    token_endpoint = 'https://api.genius.com/oauth/token'
    
    def __init__(self, access_token, *args, **kwargs):
        super().__init__(*args, *kwargs)                                
        self.access_token = access_token
    
    def get_song_info(self, song_title, artist_name):
        base_url = 'https://api.genius.com'
        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        search_url = base_url + '/search'
        data = {
            'q': song_title + ' ' + artist_name
            }
        response = requests.get(search_url, data=data, headers=headers)
        data = response.json()
        return data
        