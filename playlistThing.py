import json
import requests

endpoint_url = "https://api.spotify.com/v1/recommendations?"
token = "BQCuGEbjSpT3JhK6WW0fYXTu3BCWVugbyjK6czNYZhT4tnqO2AeA0jY615erJNQJInaqUmK3s0Kjf93tMvyWfe4FtVDAaFJ9EPeNuW8dh1aCuG-4JYjN6S9KL7yXa64rS04EtuDTKTdrnodwNXA4LLanerJuHZ0ywT4KV9yNUgEsUJljxpmacfI14kYJzrAZXbI5D191eA"
user_id = "d830be3f111a4fde99206fde7e672537"

user_genre = input("Enter genre for playlist:")
user_energy = input("Enter energy wanted for playlist (0 - 1.0 inclusive) :")
user_danceability = input("Enter danceability wanted for playlist (0 - 1.0 inclusive) :")
user_valence = input("Enter valence (high value = happy,cheerful, euphoric    low value = sad,depressed,angry) wanted for playlist (0 - 1.0 inclusive) :")

# OUR FILTERS
limit=10
market="US"
seed_genres= user_genre
target_danceability=float(user_danceability)
uris = [] 
#seed_artists = '0YhUSm86okLWldQVwJkLlP'
#seed_tracks='55SfSsxneljXOk5S3NVZIW'
target_energy = float(user_energy)
target_valence = float(user_valence)
target_duration_ms = 180000 #3 min per song

# PERFORM THE QUERY
query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'
#query += f'&seed_artists={seed_artists}'
#query += f'&seed_tracks={seed_tracks}'
query += f'&target_energy={target_energy}'
query +=  f'&target_valence={target_valence}'
query += f'&target_duration_ms={target_duration_ms}'
response = requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()
# print('Recommended Songs:')
for i,j in enumerate(json_response['tracks']):
             uris.append(j['uri'])
#             print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")










user_id = "mfrogs32"
token = "BQCuGEbjSpT3JhK6WW0fYXTu3BCWVugbyjK6czNYZhT4tnqO2AeA0jY615erJNQJInaqUmK3s0Kjf93tMvyWfe4FtVDAaFJ9EPeNuW8dh1aCuG-4JYjN6S9KL7yXa64rS04EtuDTKTdrnodwNXA4LLanerJuHZ0ywT4KV9yNUgEsUJljxpmacfI14kYJzrAZXbI5D191eA"
endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
request_body = json.dumps({
          "name": "test playlist",
          "description": "peepee",
          "public": False 
        })

response = requests.post(endpoint_url,data = request_body,
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
                        
#url = response.json()['external_urls']['spotify']
#print(response.status_code)







playlist_id = response.json()['id']
endpoint_url2 = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
          "uris" : uris
        })
response = requests.post(url = endpoint_url2, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})

print(response.status_code)