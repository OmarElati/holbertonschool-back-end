#!/usr/bin/python3
'''export data in the CSV format.'''
import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(
        f'{url}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

    if response.status_code == 200:
        data = response.json()
        user_tasks = {user_id: []}

        with open(f'{user_id}.json', 'w', encoding='utf-8') as file:
            for task in data:
                task_info = {
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': task['user']['username']
                }
                user_tasks[user_id].append(task_info)

            json.dump(user_tasks, file)

    else:
        print(f"Error: {response.status_code}")
