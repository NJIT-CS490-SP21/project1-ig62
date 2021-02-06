import requests
import os
import base64
from dotenv import load_dotenv, find_dotenv
from urllib.parse import urlencode

class SpotifyAPI(object):
    access_token = None
    client_id = None
    client_secret = None
    token_endpoint = 'https://accounts.spotify.com/api/token' 
    
    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, *kwargs)                                #prevents you from needing to rewrite methods in your subclass
        self.client_id = client_id
        self.client_secret = client_secret
    
    def convert_b64(self):                                              #converts a string into base64 encoded string
        client_id = self.client_id
        client_secret = self.client_secret
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()
    
    def get_auth(self):
        token_endpoint = self.token_endpoint
        
        token_data = {
            "grant_type": "client_credentials"
        }
        
        client_creds_b64 = self.convert_b64()
        token_headers = {
            "Authorization" : f"Basic {client_creds_b64}" 
        }
        
        spotify = requests.post(token_endpoint, data = token_data, headers = token_headers)
        
        """
        Check if authentication went through
        """
        if spotify.status_code not in range(200, 299):                        
            raise Exception("Could not authenticate client.")
        
        data = spotify.json()
        access_token = data['access_token']
        self.access_token = access_token
        return True
    
    def get_access_token(self):
        token = self.access_token
        if token == None:
            self.get_auth()
            return self.get_access_token()
        return token
    """
    def get_resource(self):
        access_token = self.get_access_token()
        headers = {
            auth_headers = {
             "Authorization": f"Bearer {access_token}"
        }
    """
    def get_artist(self, artist_query):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        search_endpoint = 'https://api.spotify.com/v1/search'
        data = urlencode({"q": {artist_query.lower()}, "type": "artist"})
        lookup_url = f"{search_endpoint}?{data}"
        artist_data = requests.get(lookup_url, headers=headers)
        artist = artist_data.json()
        return(artist)
    
    def lookup_artist_tracks(self, artist):
        id_raw = self.get_artist(artist)
        id = id_raw["artists"]["items"][0]["id"]
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        search_endpoint = f'https://api.spotify.com/v1/artists/{id}/top-tracks'
        query_params = "market=US"
        lookup_url = f"{search_endpoint}?{query_params}"
        data = requests.get(lookup_url, headers=headers)
        artist_data = data.json()
        return artist_data
    
    def lookup_tracks(self, track_id):
        track_id = track_id
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        search_endpoint = f'https://api.spotify.com/v1/tracks/{track_id}'
        data = requests.get(search_endpoint, headers=headers)
        track_data = data.json()
        return track_data
        
        
        
        
        
