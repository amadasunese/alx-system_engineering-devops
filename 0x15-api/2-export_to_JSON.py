#!/usr/bin/python3

# export data in the JSON format.

import requests
import json

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

            # Create JSON data
            json_data = {
                "USER_ID": [{"task": task['title'], "completed": task['completed'], "username": employee_name} for task in todo_data]
            }

            # Writing data to JSON file
            json_filename = f"{employee_id}.json"
            with open(json_filename, 'w') as json_file:
                json.dump(json_data, json_file, indent=4)

            print(f"\nData exported to {json_filename}")

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
