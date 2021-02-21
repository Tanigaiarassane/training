import json
import requests

# Creating dictionary of header
# Sending headers with request
# https://httpbin.org/get - return header content in response

url = 'https://httpbin.org/get'

header_data = {'first':'first', 'second':'second'}
response = requests.get(url, headers = header_data)
print(response.text)