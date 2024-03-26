#!/usr/bin/python3
"""
Return information for a given employee ID.

About his/her TODO list progress from a REST API.
"""

import json
from sys import argv

import requests


def fetch_data(id):
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(id))
    user = req.json()

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(id))
    todos = req.json()
    task_list = []
    for todo in todos:
        task = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user["username"],
        }
        task_list.append(task)

    data = {str(user["id"]): task_list}
    filename = "{}.json".format(user["id"])
    with open(filename, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    fetch_data(argv[1])
