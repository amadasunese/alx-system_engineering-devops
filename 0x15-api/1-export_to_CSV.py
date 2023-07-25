#!/usr/bin/python3

# Python script to export data in the CSV format

import requests
import csv

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

            # Export data to CSV file
            csv_filename = f"{employee_id}.csv"
            with open(csv_filename, mode='w', newline='') as csv_file:
                fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                for task in todo_data:
                    writer.writerow({
                        'USER_ID': employee_id,
                        'USERNAME': employee_name,
                        'TASK_COMPLETED_STATUS': task['completed'],
                        'TASK_TITLE': task['title']
                    })

            print(f"Data exported to {csv_filename}")

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
