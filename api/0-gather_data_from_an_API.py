#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API."""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])

    user = requests.get(
        "{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}).json()

    name = user.get("name")
    done = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title"))),
        
