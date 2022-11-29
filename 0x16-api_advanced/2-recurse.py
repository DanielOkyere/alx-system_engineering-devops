#!/usr/bin/python3
"""
Queries using recursive
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts
    recursively
    Args:
        subreddit(string): name of the subreddit
        hot_list(list): list of current hotlist
        count(int): number of current count

    Returns:
        hot_list

    """
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(
        subreddit
    )
    headers = {
        'after': after,
        'count': count,
        'limit': 100
    }

    data = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if data.status_code == 404:
        return None

    res = data.json().get('data')
    after = res.get('after')
    count += res.get('dist')

    for c in res.get('children'):
        hot_list.append(c.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
