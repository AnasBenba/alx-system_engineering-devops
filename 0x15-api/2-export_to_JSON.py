#!/usr/bin/python3
"""Exports data to JSON format"""

import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    username = response.json().get('username')
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = requests.get(url)
    tasks = response.json()
    dictionary = {user_id: []}
    for task in tasks:
        dictionary[user_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open(f'{user_id}.json', 'w') as file:
        json.dump(dictionary, file)
