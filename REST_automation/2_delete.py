#Delete Resource - use delete method of api
import requests

url = 'https://reqres.in/api/users/2'
response = requests.delete(url) # In actual they are not deleting it in reqes.in as this is a sample site

assert response.status_code == 204
