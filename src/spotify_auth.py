import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
load_dotenv()


CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_KEY = os.getenv('SPOTIPY_CLIENT_SECRET_ID')
#print(f'{CLIENT_ID}, {CLIENT_KEY}')
REDIRECT_URI = 'http://example.com'
SCOPE = 'playlist-modify-private'

sp_oauth = spotipy.SpotifyOAuth(scope = SCOPE, redirect_uri = REDIRECT_URI,
                     client_id = CLIENT_ID, client_secret = CLIENT_KEY,
                     show_dialog = True, cache_path = 'token.txt',)

#Get the access token:
token = sp_oauth.get_access_token(as_dict = False)

#Creating spotify object with the access token.
sp = spotipy.Spotify(auth=token)

#Fetch the current user's profile
user_profile = sp.current_user()

#Fetching the id
#user_id = user_profile['id']
#print(user_id)
