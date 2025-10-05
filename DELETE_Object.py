import requests
import json

base_url = "https://api.restful-api.dev"
auth_token = "Bearer "

def del_req():
    url = base_url + "/objects/6"
    response_del = requests.delete(url=url)
    assert response_del.status_code == 200, "Status code not matched with 200"
    json_get_data = response_del.json()
    json_get_str = json.dumps(json_get_data, indent=4)
    print("Json body response for get data", json_get_str)

del_req()