# API advanced

Python scripts that query the Reddit API using the `requests` module.

| File | Description |
| --- | --- |
| `0-subs.py` | `number_of_subscribers(subreddit)` returns a subreddit's total subscribers (0 if invalid). |
| `1-top_ten.py` | `top_ten(subreddit)` prints the titles of the first 10 hot posts (`None` if invalid). |
| `2-recurse.py` | `recurse(subreddit, hot_list=[])` recursively returns a list of all hot post titles (`None` if invalid). |
| `3-count.py` | `count_words(subreddit, word_list)` recursively counts keywords in hot post titles and prints a sorted count. |

All requests send a custom `User-Agent` and do not follow redirects
(`allow_redirects=False`), so an invalid subreddit is detected instead of
being redirected to a search page.
