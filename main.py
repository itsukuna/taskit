import json
import os
import sys
from datetime import datetime
from pprint import pprint

task_file = 'tasks.json'

def load_tasks():
    if not os.path.exists(task_file):
        return []
    with open(task_file, 'r') as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(task_file, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = max([task['id'] for task in tasks], default=0) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'to-do',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    pprint(f'Task added: {task}')

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task['status'] == filter_status]
    for task in tasks:
        print(task)

def update_task(task_id, description=None, status=None):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if description:
                task['description'] = description
            if status:
                task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f'Task updated: {task}')
            return
    print(f"Task with id {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    tasks=[task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f'Task with id {task_id} deleted')

def main():
    if len(sys.argv) < 2:
        print('Usage: main.py <command> [<args>]')
        return
    command = sys.argv[1]
    match command:
        case 'add':
            add_task(sys.argv[2])
        case 'list':
            list_tasks(sys.argv[2] if len(sys.argv) > 2 else None)
        case 'update':
            update_task(int(sys.argv[2]), sys.argv[3] if len(sys.argv) > 3 else None, sys.argv[4] if len(sys.argv) > 4 else None)
        case 'delete':
            delete_task(int(sys.argv[2]))
        case _:
            print(f'Unkown command {command}')


if __name__ == '__main__':
    main()