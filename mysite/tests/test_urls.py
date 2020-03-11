from rest_framework.test import RequestsClient


client = RequestsClient()
response = client.get('http://0.0.0.0/colors')
assert response.status_code == 200