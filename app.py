import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

#unique username from spotify
username = "mfrogs32"

#application details
SPOTIPY_CLIENT_ID='d830be3f111a4fde99206fde7e672537'
SPOTIPY_CLIENT_SECRET='ac50a089f6f3400e8d437f7973c2f2ba'
SPOTIPY_REDIRECT_URI= 'http://127.0.0.1:9090'
SCOPE = "playlist-modify-private playlist-read-private"

#authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

#printing available genres to user
genres = sp.recommendation_genre_seeds()
print("~~~~~~~~~~~~~~~~~~~")
print(f"AVAILABLE GENRES: ")
print("~~~~~~~~~~~~~~~~~~~")
for i,j in enumerate(genres['genres']):
            #uris.append(j['uri'])
            print(f"[{j}]", end= "  -  ")
print("")
print("")


#USER PROMPTS TO GET PREFS
playlist_name = input("Enter name for playlist: ")
playlist_description = input("Enter small description of playlist: ")
user_genre = input("Genre (up to 5 comma seperated, no spaces): ")
user_energy = input("Enter energy wanted for playlist (0 - 1.0 inclusive): ")
user_danceability = input("Enter danceability wanted for playlist (0 - 1.0 inclusive): ")
user_valence = input("Enter valence (high value = happy,cheerful, euphoric    low value = sad,depressed,angry) wanted for playlist (0 - 1.0 inclusive): ")

# OUR FILTERS FOR RECOMMENDATION SONGS
limit1=50
market1="US"
seed_genres1= user_genre.split(',')
target_danceability1 =float(user_danceability)
uris = [] 
#seed_artists = '3TVXtAsR1Inumwj472S9r4'
#seed_tracks='55SfSsxneljXOk5S3NVZIW'
target_energy1 = float(user_energy)
target_valence1 = float(user_valence)
#target_duration_ms = 180000 #3 min per song

#RECOMMENDATION LIST OF SONGS
recs = sp.recommendations(seed_tracks=None,seed_artists=None,seed_genres = seed_genres1,country = market1,limit = limit1, target_energy = target_energy1, target_danceability = target_danceability1, target_valence = target_valence1 )

#get the unique spotify track uri for a complete list of the songs to add to the playlist
for i,j in enumerate(recs['tracks']):
              uris.append(j['uri'])

#create playlist on user profile with unique names
sp.user_playlist_create(username,playlist_name, public = False, collaborative=False, description = playlist_description)

#iterate through user playlists for unique playlist ID
playlist_id = ''
playlist_link = ''
playlists = sp.user_playlists(username)
for playlist in playlists['items']:  # iterate through playlists I follow
    if playlist['name'] == playlist_name:  # filter for newly created playlist
        playlist_id = playlist['id']
        playlist_link = playlist['external_urls']

#get link of new playlist
playlist_finalLink = playlist_link['spotify']

#add the songs with the list of uris we got earlier
sp.user_playlist_add_tracks(username, playlist_id, uris)

#print the playlist to user
print(f"{playlist_name} can be found at: {playlist_finalLink}")
