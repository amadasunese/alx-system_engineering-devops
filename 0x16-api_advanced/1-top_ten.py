#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles of the first 10 hot posts 
"""

import requests


def top_ten(subreddit):
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python/1.0(Holberton School 0x16)'}  # Add your custom user agent here
    
    try:
        response = requests.get(base_url, headers=headers, params={'limit': 10})
        response.raise_for_status()  # Check for any HTTP error

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

# Call the function with the desired subreddit name
top_ten("python")
