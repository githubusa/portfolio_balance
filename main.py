import requests

"""
This is program is used to test distribute python project
with pipenv and requests

"""
response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
