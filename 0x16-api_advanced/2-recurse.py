#!/usr/bin/python3
'''
Module 2-recurse
retrieve list containing titlesof hot articles for a given subreddit
'''
import requests


def recurse(subreddit, hot_list=[], after='tmp'):
    '''
    recursvily get hot artilce titles for subreddit
    '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'linux'}
    if after != 'tmp':
        url = url + '?after={}'.format(after)

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        return None
    res = r.json().get('data')
    res = res.get('children')
    if not res:
        return hot_list
    'apend artils to list'
    for a in res:
        hot_list.append(a.get('data').get('title'))
        'get next param'
    after = r.get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
