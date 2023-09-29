#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    data = {"q": ""}
    data["q"] = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        json_body = r.json()
        if not json_body:
            print("No result")
        else:
            print("[{}] {}".
                  format(json_body.get('id'), json_body.get('name')))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
