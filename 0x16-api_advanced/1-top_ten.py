#!/usr/bin/python3
"""
This module contains function that queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """ Prints the top ten hot posts of a subreddit """
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False,
    )
    if res.status_code != 200:
        print(None)
        return
    dic = res.json()
    hot_posts = dic['data']['children']
    if hot_posts == 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
