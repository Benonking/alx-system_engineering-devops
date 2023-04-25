#!/usr/bin/python3
"""
fetch data from API and export to csv file
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    ID = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + ID
    user_dict = requests.get(user_url).json()
    name = user_dict.get("username")
    user_todo = requests.get("{}/todos".format(user_url)).json()
    csv_file = ID + ".csv"

    with open(csv_file, 'w') as f:
        for item in user_todo:
            f.write('"{}","{}","{}","{}"\n'
                    .format(item.get("userId"), name,
                            item.get("completed"), item.get("title")))
