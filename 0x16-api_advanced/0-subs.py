#!/usr/bin/python3
"""
Module 0-subs
Contains function def number_of_subscribers(subreddit)
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "linux:alx_app:v1.0.0 (by /u/Icy_Advice_679)"
    }

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful and the subreddit exists
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the subreddit doesn't exist or there's an error, return 0
            return 0
    except Exception as e:
        # If any exception occurs (e.g., network error), return 0
        return 0