#!/usr/bin/python3
"""get request reddit api"""
import requests


def recurse(subreddit, hot_list=[], page=None):
    """function that print the titles of the 10 hottest posts"""
    headers = {"User-Agent": "geraldinnebohr"}

    if page:
        sub = requests.get('https://reddit.com/r/' + subreddit +
                           '/hot.json?after=' + page,
                           headers=headers)
    else:
        sub = requests.get('https://reddit.com/r/' + subreddit +
                           '/hot.json', headers=headers)

    if sub.status_code == 404:
        return None

    sub_json = sub.json()
    sub_data = sub_json['data']
    page = sub_data['after']
    sub_children = sub_data['children']

    for children in sub_children:
        children_data = children['data']
        hot_list.append(children_data['title'])

    if page:
        recurse(subreddit, hot_list, page)
    return hot_list
