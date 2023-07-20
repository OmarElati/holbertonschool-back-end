#!/usr/bin/python3
'''export data in the CSV format.'''
import csv
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
        user_name = data[0]['user']['username']

        with open(f'{user_id}.csv', 'w', encoding='utf-8', newline='') as file:
            wr = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in data:
                wr.writerow(
                    [
                        f'{user_id}',
                        f'{user_name}',
                        f'{task["completed"]}',
                        f'{task["title"]}'
                    ]
                )

    else:
        print(f"Error: {response.status_code}")
