#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    params = {"q": letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=params)
    try:
        json_response = r.json()
        if not json_response:
            print("No result")
        else:
            user_data = json_response[0]
            print("[{}] {}".
                  format(user_data.get('id'), user_data.get('name')))
    except ValueError:
        print("Not a valid JSON")
