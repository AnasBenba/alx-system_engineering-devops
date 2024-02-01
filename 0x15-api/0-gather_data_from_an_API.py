#!/usr/bin/python3
"""Fetch data from an API"""

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos')
    my_user = user.json()
    todo = todos.json()
    done = 0
    num_of_t = 0
    for t in todo:
        if t['completed']:
            done += 1
        num_of_t += 1
    print(f'Employee {my_user["name"]} is done with tasks({done}/{num_of_t}):')
    for t in todo:
        if t['completed']:
            print(f"\t {t['title']}")
