#!/usr/bin/python3
"""
Return information for a given employee ID.

About his/her TODO list progress from a REST API.
"""

import csv
from sys import argv

import requests


def fetch_data(id):
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(id))
    user = req.json()

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(id))
    todos = req.json()

    filename = "{}.csv".format(user["id"])
    with open(filename, "w") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user["id"], user["username"],
                            todo["completed"], todo["title"]])


if __name__ == "__main__":
    fetch_data(argv[1])
