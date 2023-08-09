#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles
"""

import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit=10'.format(
        subreddit)
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16)'}

    try:
        response = requests.get(url, headers=headers,
                                params={'limit': 10})
        response.raise_for_status()

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("No posts found.")
        else:
            for post in posts:
                title = post['data']['title']
                print(title)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


top_ten("python")
