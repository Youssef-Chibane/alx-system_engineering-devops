#!/usr/bin/python3
'''
A script that contains a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers) for
a given subreddit.
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Returns the number of subcribers for a given valid subreddit or 0 if
    subreddit is invalid
    '''
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
