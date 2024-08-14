#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        return top ten titles for a given subreddit
        return None if invalid subreddit given
    """
    headers = {
        "User-Agent": "linux:alx_app:v1.0.0 (by /u/Icy_Advice_679)"
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers=headers).json()
    top_ten = r.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for t in top_ten:
        print(t.get('data').get('title'))
