#!/usr/bin/python3
"""Expanded to Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todo = requests.get('https://jsonplaceholder.typicode.com/todo')
    todo = todo.json()

    todoUser = {}
    taskList = []

    for task in todo:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
