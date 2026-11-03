#!/usr/bin/python3
"""
Python script to export TODO list data of all employees in JSON format.
"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"

    users_res = requests.get(f"{base_url}users")
    users = users_res.json()

    todos_res = requests.get(f"{base_url}todos")
    todos = todos_res.json()

    all_data = {}

    for user in users:
        emp_id = user.get("id")
        username = user.get("username")

        user_todos = [t for t in todos if t.get("userId") == emp_id]
        task_list = []

        for task in user_todos:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            task_list.append(task_dict)

        all_data[str(emp_id)] = task_list

    with open("todo_all_employees.json", mode="w", encoding="utf-8") as f:
        json.dump(all_data, f)
