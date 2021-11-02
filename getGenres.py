import requests



# SETTINGS 
endpoint_url = "https://api.spotify.com/v1/recommendations/available-genre-seeds"
token = "BQDr2L71FpQbLRrU3bwmRWJV3kdJ-uAVpEkOz4DdLmGIs1t-3_Y36JrWBZoZ7RSdZFqxCs7JILLcqIelrebYjlzroacEuZklgpKgbPK-mZewGc2E1Hj01Hsyc4lRlQS0B_DEeapWF0Lvxr_bD2caqSDg_rN2YzSpp82pZYk8AZZw"
user_id = "d830be3f111a4fde99206fde7e672537"

response = requests.get(endpoint_url,
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()
#print(json_response)
for i,j in enumerate(json_response['genres']):
            #uris.append(j['uri'])
            print(f"[{j}]", end= "  -  ")