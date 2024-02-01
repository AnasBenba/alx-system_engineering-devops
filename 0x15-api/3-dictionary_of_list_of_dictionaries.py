#!/usr/bin/python3
"""Exports data in JSON format"""

import json
import requests

if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo = todos.json()
    data = {}
    id = str(todo[0]['userId'])
    data[id] = []
    my_user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    for t in todo:
        record = {
            "username": my_user['username'],
            "task": t['title'],
            "completed": t['completed']}
        if str(t['userId']) == id:
            data[id].append(record)
        else:
            id = str(t['userId'])
            data[id] = []
            my_user = requests.get(
                f'https://jsonplaceholder.typicode.com/users/{id}').json()
            record = {
                "username": my_user['username'],
                "task": t['title'],
                "completed": t['completed']}
            data[id].append(record)
    with open(f'todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
