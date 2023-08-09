#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            return hot_list
        else:
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            after = data.get('data', {}).get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None


subreddit_name = "python"
hot_titles = recurse(subreddit_name)

if hot_titles is None:
    print("No results found for the subreddit.")
else:
    for index, title in enumerate(hot_titles, start=1):
        print(f"{index}. {title}")
