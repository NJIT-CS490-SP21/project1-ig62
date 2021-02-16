# Project 1

Ian Gabrielle Gojo Cruz  
CS 490 - 004  

## Description

This project is for CS 490 class at NJIT.  
This is a simple _music discovery_ webapp that utilize third-party APIs from [Spotify](https://developer.spotify.com/) and [Genius](https://docs.genius.com/).  

## Language and Libraries
1. Python
2. Flask
3. HTML
4. CSS
5. Heroku

## Installation  
### 1. Install python.  

You can check your `python` version using the command below.  
```bash
$ python --version
```
Installing python3 in linux.  
```bash
$ sudo apt-get update
$ sudo apt-get install python3.6
```
### 2. Install flask.  
```bash
pip install Flask
```
*Note*: You can use `sudo` command if there are any problems in the `flask` installation process.

### 3. Sign-up for a [Spotify Developer](https://developer.spotify.com/) and [Genius](https://docs.genius.com/#/getting-started-h1) and create your app.  
### 4. Create a `.env` file in the same directory as you `app.py` file with the following commands.  
#### Spotify
```
export CLIENT_ID='<Your Client ID>'
export CLIENT_SECRET='<Your Client Secret>'
```

#### Genius
```
export HACCESS_TOKEN='<Your Access Token>'
```
*Note:* You can generate your access token at Genius' website.  
*Note:* Both are saved on the same `.env` file.

### 5. Run your `app.py` and have fun listening!
*Note*: You can hardcode a list of your 3 favorite artist inside `app.py` on ` line 22`.

### 6. Heroku Deployment  
- Install heroku using the following command.
```bash
npm install -g heroku
```
- Sign up for a [Heroku](https://signup.heroku.com/login) account.
- Add and commit all changed files using git.  
- On your terminal, login to heroku using the following command.  
```bash
heroku login -i
```
- Create your new heroku app using the following command.  
```bash
heroku create
```
- Push your code to heroku.  
```bash
git push heroku main
```
- Add your `.env` variables in your heroku [dashboard](https://dashboard.heroku.com/apps) then go to **Settings** and click **Reveal Config Vars**.  
- Add your keys with the matching variable names (No quotes).
- Check your own URL!



## Known Problems and Solutions

### 1. Problem where my `CLIENT_ID` and `CLIENT_SECRET` did not load from my `.env` file.   
*Solution* - I realized that I missed a code that loads `.env` file into my python program.  
```python
load_dotenv(find_dotenv())
```
### 2. `preview_url` is set to None for some cases when getting an artist's track information using `lookup_artist_tracks`.   
*Solution* - I made a separate function to search for that specific track using the `track_id` from the `.json` data provided in `lookup_artist_tracks`.  
```python
def lookup_tracks(self, track_id):
        track_id = track_id
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        search_endpoint = f'https://api.spotify.com/v1/tracks/{track_id}'
        data = requests.get(search_endpoint, headers=headers)
        track_data = data.json()
        return track_data
```
*Note:* Some tracks might not have any preview depending on the `market`  

### 3. Images that are stored locally weren't being uploaded properly. 
This is a temporary solution: Upload the image on a picture hosting website such as [imgur](https://imgur.com)

### 4. I'm getting an access token error with genius.
*Solution* - Generate a new key on genius' website.
