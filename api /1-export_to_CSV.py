import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com/"

        user_res = requests.get(f"{base_url}users/{emp_id}")
        user_data = user_res.json()
        username = user_data.get("username")

    
        todos_res = requests.get(f"{base_url}todos?userId={emp_id}")
        todos = todos_res.json()

        task_list = []
        for task in todos:
            task_dict = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
            task_list.append(task_dict)

        data_to_export = {str(emp_id): task_list}

        filename = f"{emp_id}.json"
        with open(filename, mode="w", encoding="utf-8") as f:
            json.dump(data_to_export, f)
