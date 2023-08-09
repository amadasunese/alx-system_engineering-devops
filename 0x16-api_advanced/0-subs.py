#!/usr/bin/python3
# A function that queries the Reddit API and returns the number of subscribers 
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid API rate limiting issues
    headers = {'User-Agent': 'CustomUserAgent'}

    # Construct the URL for the subreddit's about page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Make the API request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()

            # Extract the subscriber count from the JSON data
            subscribers = data['data']['subscribers']

            return subscribers
        except (KeyError, ValueError):
            # Invalid JSON or missing data, return 0
            return 0
    elif response.status_code == 302:
        # Redirect, likely an invalid subreddit
        return 0
    else:
        # Other error, return 0
        return 0

# Test the function
subreddit_name = "programming"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
