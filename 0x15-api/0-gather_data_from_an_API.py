#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
if __name__ == "__main__":
    ID = argv[1]
    url = 'https://jsonplaceholder.typicode.com/todos'.format(ID)
    todos = get(url, params={"userId": ID}).json()
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(ID)
    user = get(user_url).json()
    name = user.get('name')
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(completed), len(todos)))
    [print('\t {}'.format(t)) for t in completed]
