#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot posts."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the given keywords in hot post titles.

    Keywords are case-insensitive and must match whole space-delimited
    words. Duplicate keywords in word_list add up. Results are printed in
    descending order of count, then alphabetically. Prints nothing if the
    subreddit is invalid or nothing matches.
    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0 (by /u/alu_dev)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return

    keywords = [word.lower() for word in word_list]
    for child in data.get("children", []):
        title = child.get("data", {}).get("title") or ""
        for token in title.lower().split():
            if token in keywords:
                counts[token] = counts.get(token, 0) + keywords.count(token)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    for word, total in ranked:
        if total > 0:
            print("{}: {}".format(word, total))
