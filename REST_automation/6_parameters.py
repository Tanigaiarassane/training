# parameters in requesets
# create dictionary of parameters
# send it through get requests

import requests

params = {"name": "python training" }

url = 'https://httpbin.org/get'

response = requests.get(url, params=params)
print(response.text)