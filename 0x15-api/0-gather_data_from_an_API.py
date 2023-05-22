#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    todos = get(url + 'todos', params={"userId": argv[1]}).json()
    user = get(url + 'users/{}'.format(argv[1])).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completed), len(todos)))
    [print('\t {}'.format(t)) for t in completed]
