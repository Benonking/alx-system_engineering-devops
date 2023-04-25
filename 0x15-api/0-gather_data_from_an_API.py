#!/usr/bin/python3
"""
python script that uses REST API,
for a given employee Id
Returns: To do list progresss
"""
import requests
from sys import argv

if __name__ == "__main__":
    ID = argv[1]
    user_urli = "https://jsonplaceholder.typicode.com/users/" + ID

    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("name")
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_todo = requests.get(todo_url).json()

    task_todo = 0
    task_complete = 0
    completed_titles = []

    for item in user_todo:
        if item.get('ID') == int(ID):
            task_todo += 1
            if item.get("completed") is True:
                task_complete += 1
                completed_titles.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, task_complete, task_todo))

    for title in completed_titles:
        print("\t {}".format(title))
