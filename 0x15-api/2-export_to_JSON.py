#!/usr/bin/python3
"""Exports data to JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos')
    my_user = user.json()
    todo = todos.json()
    data = {f"{id}": []}
    for t in todo:
        record = {
            "task": t['title'],
            "completed": t['completed'],
            "username": my_user['username']}
        data[id].append(record)
        with open(f'{id}.json', 'w') as json_file:
            json.dump(data, json_file)
