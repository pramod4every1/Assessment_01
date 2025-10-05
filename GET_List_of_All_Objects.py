import requests
import json

base_url = "https://api.restful-api.dev"
auth_token = "Bearer "

def get_req():
    url = base_url + "/objects"
    response_get = requests.get(url=url)
    assert response_get.status_code == 200, "Status code not matched with 200"
    json_get_data = response_get.json()
    json_get_str = json.dumps(json_get_data, indent=4)
    print("Json body response for get data", json_get_str)


get_req()