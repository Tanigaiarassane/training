import requests
import jsonpath
import json
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
assert response.status_code, 200


#Fetch Response header value
#Response has header and body
# Fetch Complete respose header
print(response.headers)


#Fetch specific header content
print(response.headers.get('Date'))
print(response.headers.get('server'))

#Featch cookies
print(response.cookies)

#Fetch encoding
print(response.encoding)

#Fetch elapsed time - time taken between the request sent and response received
print(response.elapsed)

## Fetching response usong jsonpath
#Fetch response content
print(response.content)

#parse response to json format
json_response = json.loads(response.text)
print(json_response)

#Fetch values using jsonpath
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])
assert (pages[0], 2)

#Advance json path
first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(first_name)

#fetch all first names
for i in range(0,2):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i) +'].first_name')
    print(first_name[0])