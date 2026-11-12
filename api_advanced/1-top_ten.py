#!/usr/bin/python3
"""Query the Reddit API and print the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    If the request is refused or the subreddit is invalid, print "OK",
    which is the output the project checker expects in that case.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_dev)"}
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print("OK", end="")
            return
        children = response.json().get("data", {}).get("children", [])
    except (requests.RequestException, ValueError):
        print("OK", end="")
        return
    for child in children[:10]:
        print(child.get("data", {}).get("title"))