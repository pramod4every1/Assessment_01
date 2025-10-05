import requests
import json

base_url = "https://api.restful-api.dev"
auth_token = "Bearer "


def patch_request():
    url = base_url + "/objects/7"
    data = {
         "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response_patch = requests.put(url=url, json=data)
    print("Response code is ",response_patch.status_code)
    json_patch_data = response_patch.json()
    json_patch_str = json.dumps(json_patch_data, indent=4)
    print("Post Response body: ", json_patch_str)
    assert response_patch.status_code == 200, "Status code not matched with 200"

patch_request()