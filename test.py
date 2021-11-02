import requests

# SETTINGS 
endpoint_url = "https://api.spotify.com/v1/recommendations?"
token = "BQDr2L71FpQbLRrU3bwmRWJV3kdJ-uAVpEkOz4DdLmGIs1t-3_Y36JrWBZoZ7RSdZFqxCs7JILLcqIelrebYjlzroacEuZklgpKgbPK-mZewGc2E1Hj01Hsyc4lRlQS0B_DEeapWF0Lvxr_bD2caqSDg_rN2YzSpp82pZYk8AZZw"
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
# print(json_response)
print('Recommended Songs:')
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")