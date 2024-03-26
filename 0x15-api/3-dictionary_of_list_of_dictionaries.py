#!/usr/bin/python3
"""
Return information for a given employee ID.

About his/her TODO list progress from a REST API.
"""

import json

import requests


def save_data_to_json():
    data = {}
    for id in range(1, 11):
        req = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(id))
        user = req.json()
        req = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        )
        todos = req.json()
        task_list = []
        for todo in todos:
            task = {
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"],
            }
            task_list.append(task)
        data[str(user["id"])] = task_list

    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    save_data_to_json()
