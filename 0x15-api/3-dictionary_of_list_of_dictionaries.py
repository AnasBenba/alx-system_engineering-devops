#!/usr/bin/python3
"""Exports data in JSON format"""

import json
import requests

if __name__ == '__main__':
    users_url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(users_url)
    users = response.json()
    dictionary = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        u_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos/'
        response = requests.get(u_url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
