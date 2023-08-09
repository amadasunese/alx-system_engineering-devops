#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
import requests
"""
import requests


def number_of_subscribers(subreddit):

    headers = {'User-Agent': 'CustomUserAgent'}

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()

            subscribers = data['data']['subscribers']

            return subscribers
        except (KeyError, ValueError):
            return 0
    elif response.status_code == 302:
        return 0
    else:
        return 0


subreddit_name = "programming"
subscribers_count = number_of_subscribers(subreddit_name)
print("The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
