#!/usr/bin/python3
"""get request reddit api"""
import requests


def top_ten(subreddit):
    """function that print the titles of the 10 hottest posts"""
    headers = {"User-Agent": "geraldinnebohr"}
    title = requests.get('https://reddit.com/r/' + subreddit +
                         '/hot.json?sort=hot&limit=10', headers=headers)
    if title.status_code == 404:
        print(None)
    title_json = title.json()
    title_data = title_json['data']
    title_children = title_data['children']
    for children in title_children:
        children_data = children['data']
        children_title = children_data['title']
        print(children_title)
