#!/usr/bin/python3
"""Recursively query the Reddit API for the titles of all hot posts."""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Return a list of titles of all hot posts, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_dev)"}
    params = {"limit": 100, "count": count}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return None
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return None

    children = data.get("children", [])
    titles = list(map(lambda c: c.get("data", {}).get("title"), children))
    # Build a new list so the mutable default argument is never modified
    hot_list = hot_list + titles

    after = data.get("after")
    if after is None:
        return hot_list if len(hot_list) > 0 else None
    return recurse(subreddit, hot_list, after, count + len(children))
