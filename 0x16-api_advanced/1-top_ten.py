#!/usr/bin/python3
"""
A function that print top ten titles from reddit
"""
import requests


def top_ten(subreddit):
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        response = requests.get(base_url, params={'limit': 10})
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
