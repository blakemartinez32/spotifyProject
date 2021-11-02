import requests



# SETTINGS 
endpoint_url = "https://api.spotify.com/v1/recommendations/available-genre-seeds"
token = "BQCRj_lgC2YgcWx79xlYNKtPxpASmk5qBB6eXF8ppq2R2C6FvuBR23CiJneGPUyahZuX1Rclb1Hzbh_Z1bszJcDrmF2mKge5VeHvQF7U1eoDhrbHv1xx6INY_rc1K-4veWjFPnVs_ZYkJArRobGRQHOWi3yJfytlUYFzzHhDBBvP4ig"
user_id = "d830be3f111a4fde99206fde7e672537"

response = requests.get(endpoint_url,
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {token}"})
json_response = response.json()
#print(json_response)
for i,j in enumerate(json_response['genres']):
            #uris.append(j['uri'])
            print(f"[{j}]", end= "  -  ")