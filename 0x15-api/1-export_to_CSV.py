#!/usr/bin/python3
"""Exports to CSV"""

import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(user_url)
    username = user_response.json().get('username')
    u = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    tasks_response = requests.get(u)
    tasks = tasks_response.json()
    csv_filename = '{}.csv'.format(user_id)
    with open(csv_filename, 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, username, task.get('completed'),
                               task.get('title')))
