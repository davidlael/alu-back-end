
import csv
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

        filename = f"{emp_id}.csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow(
                    [
                        str(emp_id),
                        username,
                        str(task.get("completed")),
                        task.get("title"),
                    ]
                )
