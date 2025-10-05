import requests
import json

base_url = "https://api.restful-api.dev"
auth_token = "Bearer "


def put_request():
    url = base_url + "/objects/7"
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
            }
    }
    response_put = requests.put(url=url, json=data)
    print("Response code is ",response_put.status_code)
    json_put_data = response_put.json()
    json_put_str = json.dumps(json_put_data, indent=4)
    print("Post Response body: ", json_put_str)
    assert response_put.status_code == 200, "Status code not matched with 200"

put_request()