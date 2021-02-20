import requests
import jsonpath

#reqres.in - Sample request uri for practising

url = "https://reqres.in/api/users?page=2"

#request using GET method

response = requests.get(url)

print(response) # returns response object with status code
print(response.status_code) #status code
print(response.content) # Body of the response object
print(response.headers) # Headers from response object


#validate status code, response content
# First we need to validate http status code
# 2xx, 3xx,4xx, 5xx
