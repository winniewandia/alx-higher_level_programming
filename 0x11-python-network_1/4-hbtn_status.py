#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)
data = response.text
print('Body response:')
print('\t- type: {}'.format(type(data)))
print('\t- content: {}'.format(data))
