#!/usr/bin/python3
"""
this doc for module
"""
import requests

header = {
    "User-Agent": "MyCustomUserAgent/1.0"
}


def number_of_subscribers(subreddit):
    """method doc"""
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        response = requests.get(url, allow_redirects=False, headers=header)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        return 0
    except Exception:
        return 0
