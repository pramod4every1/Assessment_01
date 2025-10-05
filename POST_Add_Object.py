import requests
import json

base_url = "https://api.restful-api.dev"
auth_token = "Bearer "



def post_request1():
    url = base_url + "/objects"
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
            }
    }
    response_post = requests.post(url=url, json=data)

    assert response_post.status_code == 200, "Status code not matched with 200"
    json_post_data = response_post.json()
    json_post_str = json.dumps(json_post_data, indent=4)
    print("Post Response body: ", json_post_str)


post_request1()

def post_request2():
    url = base_url + "/objects"
    data = {

        "name": "Apple MacBook Pro 16",
        "data": {
            "year": "2019",
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
            }
    }
    response_post = requests.post(url=url, json=data)

    assert response_post.status_code == 201, "Year Cannot be a str"
    json_post_data = response_post.json()
    json_post_str = json.dumps(json_post_data, indent=4)
    print("Post Response body: ", json_post_str)

post_request2()

def post_request3():
    url = base_url + "/objects"
    data = {

        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": "1849.99",
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
            }
    }
    response_post = requests.post(url=url, json=data)

    assert response_post.status_code == 201, "Price Cannot be a string"
    json_post_data = response_post.json()
    json_post_str = json.dumps(json_post_data, indent=4)
    print("Post Response body: ", json_post_str)

post_request3()