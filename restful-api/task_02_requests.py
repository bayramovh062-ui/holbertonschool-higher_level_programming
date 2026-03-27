#!/usr/bin/python3
"""
this module contains two function the first one for
fetch data from api and prints this data
the other one fetch data and save it to a file with csv format
"""


import csv
import requests


def fetch_and_print_posts():
    """
    this function fetchs data from api and prints them
    """

    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        for user in data:
            print(user["title"])


def fetch_and_save_posts():
    """
    this function fetchs data from api and save it to a file with
    csv format.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        filtered_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in data
        ]
        with open("posts.csv", "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered_data)
