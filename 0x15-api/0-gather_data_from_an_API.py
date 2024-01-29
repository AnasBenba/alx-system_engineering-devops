#!/usr/bin/python3
"""Fetch data from an API"""

import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user_url = base_url + "users/{}".format(user_id)
    user = requests.get(user_url).json()
    todos_url = base_url + "todos"
    todos_params = {"userId": user_id}
    todos = requests.get(todos_url, params=todos_params).json()
    completed_tasks = [task.get("title") for task in todos
                       if task.get("completed")]
    print("Employee {} has completed tasks: {}/{}".format(
        user.get("name"), len(completed_tasks), len(todos)
    ))
    for task_title in completed_tasks:
        print("\t{}".format(task_title))
