#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = requests.get(url + "users/{}".format(argv[1])).json()
    all = requests.get(url + "todos", params={"userId": argv[1]}).json()
    completed_tasks = []
    for task in all:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user_id.get('name'), len(completed_tasks), len(all)))
    for task in completed_tasks:
        print("\t {}".format(task))
