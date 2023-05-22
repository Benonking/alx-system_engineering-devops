#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    res_todos = get('https://jsonplaceholder.typicode.com/todos/')
    todos = res_todos.json()
    completed = 0
    total = 0
    tasks = []
    res_users = get('https://jsonplaceholder.typicode.com/users')
    users = res_users.json()

    for i in users:
        if i.get('id') == int(argv[1]):
            employee_name = i.get('name')

    for i in todos:
        if i.get('userId') == int(argv[1]):
            total += 1
            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed,
                                                          total))

    for i in tasks:
        print("\t {}".format(i))
