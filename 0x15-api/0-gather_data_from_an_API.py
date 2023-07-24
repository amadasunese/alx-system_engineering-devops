#!/usr/bin/python3
# Python script that, using this REST API, for a given employee ID, 
# returns information about his/her TODO list progress.

import requests

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        # Fetch employee data
        response = requests.get(f'{base_url}/{employee_id}')
        response_todo = requests.get(todo_url)

        if response.status_code == 200 and response_todo.status_code == 200:
            employee_data = response.json()
            todo_data = response_todo.json()

            employee_name = employee_data['name']
            total_tasks = len(todo_data)
            completed_tasks = sum(task['completed'] for task in todo_data)

            print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

            for task in todo_data:
                if task['completed']:
                    print(f"\t{task['title']}")

        else:
            print(f"Error: Unable to fetch data for Employee ID {employee_id}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer.")
