#!/usr/bin/python3
"""Exports to CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos')
    my_user = user.json()
    todo = todos.json()
    with open(f'{id}.csv', 'w') as csv_file:
        fieldnames = ["userId", "username", "completed", "title"]
        csv_writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL)
        for t in todo:
            t['username'] = my_user["username"]
            del t["id"]
            csv_writer.writerow(t)
