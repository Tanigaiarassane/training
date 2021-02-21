import requests
import json
import jsonpath

# create new resource
url = 'https://reqres.in/api/users/2'

# Read input json file
file = open("user.json", "r")
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

# Make PUT request with the data from request_json
response = requests.put(url, data=request_json)
print(response.content)

assert response.status_code == 200

# Fetch header from response
print(response.headers)

# parse response to json format
response_json = json.loads(response.text)

# Pick id using jsonpath
updated_time = jsonpath.jsonpath(response_json,"updatedAt")
print (updated_time[0])