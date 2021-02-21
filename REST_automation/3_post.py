import requests
import json
import jsonpath

# create new resource
url = 'https://reqres.in/api/users'

# Read input json file
file = open("user.json", "r")
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

# Make post request with the data from request_json

response = requests.post(url, data=request_json)
print(response.content)

assert response.status_code == 201

# Fetch header from response
print(response.headers)

# parse response to json format
response_json = json.loads(response.text)

# Pick id using jsonpath
id = jsonpath.jsonpath(response_json,"id")
print (id[0])