
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com/"
      
        user_res = requests.get(f"{base_url}users/{emp_id}")
        user_data = user_res.json()
        employee_name = user_data.get("name")
        todos_res = requests.get(f"{base_url}todos?userId={emp_id}")
        todos = todos_res.json()
        total_tasks = len(todos)
        completed_tasks = [t for t in todos if t.get("completed")]
        number_of_done = len(completed_tasks)
        print(
            f"Employee {employee_name} is done with tasks"
            f"({number_of_done}/{total_tasks}):"
        )
        for task in completed_tasks:
            print(f"\t {task.get('title')}")
