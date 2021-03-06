#!/usr/bin/python3
"""get request reddit api"""
import requests


def number_of_subscribers(subreddit):
    """function that returns the num of subscribers"""
    headers = {"User-Agent": "geraldinnebohr"}
    subs = requests.get('https://reddit.com/r/' + subreddit + '/about.json',
                        headers=headers, allow_redirects=True)
    if subs.status_code == 404:
        return 0
    subs_json = subs.json()
    subs_data = subs_json['data']
    subs_amount = subs_data['subscribers']
    return subs_amount
