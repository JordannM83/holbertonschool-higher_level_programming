#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print titles"""
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    print (r.status_code)


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save to CSV"""
    pass
