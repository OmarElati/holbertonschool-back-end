#!/usr/bin/python3
'''returns information about his/her TODO list progress.'''
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    response = requests.get(
        f'{url}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

    if response.status_code == 200:
        data = response.json()
        name = data[0]['user']['name']
        tasks_ok = [task for task in data if task['completed']]
        n_task_ok = len(tasks_ok)
        total_task = len(data)

        first_str = f"Employee {name} is done with tasks"

        print(f"{first_str}({n_task_ok}/{total_task}):")
        for task in tasks_ok:
            print(f"\t {task['title']}")

    else:
        print(f"Error: {response.status_code}")
