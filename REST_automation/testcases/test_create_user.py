import requests
import json
import jsonpath
import pytest

# single test cases pyest -v test_create_user
# All test cases test cases pytest -v
# Specific group pytest -m smoke -v -s
# Excluding a group during execution pytest -v -s -m "not smoke"
# skip a test case @pytest.skip("Not included in the execution")

@pytest.mark.smoke
def test_create_user():
    # create new resource
    url = 'https://reqres.in/api/users'

    # Read input json file
    file = open("C:\\Users\\Admin\\training\\REST_automation\\user.json", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)

    # Make post request with the data from request_json

    response = requests.post(url, data=request_json)
    print(response.content)


    # Fetch header from response
    print(response.headers)

    # parse response to json format
    response_json = json.loads(response.text)

    # Pick id using jsonpath
    id = jsonpath.jsonpath(response_json,"id")
    print (id[0])
    assert response.status_code == 201

def test_create_user_output():
    def test_create_user():
        # create new resource
        url = 'https://reqres.in/api/users'

        # Read input json file
        file = open("C:\\Users\\Admin\\training\\REST_automation\\user.json", "r")
        json_input = file.read()
        request_json = json.loads(json_input)
        print(request_json)

        # Make post request with the data from request_json

        response = requests.post(url, data=request_json)
        print(response.content)

        # Fetch header from response
        print(response.headers)