#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print titles"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print (f"Status Code: {r.status_code}")
    if r.status_code == 200:
        print (r.json())

def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save to CSV"""
    pass
