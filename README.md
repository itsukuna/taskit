# taskit
Project from Roadmap.sh

https://roadmap.sh/projects/task-tracker

## Task Tracker CLI

### Installation

Clone the repository:
```sh
pip install git+https://github.com/itsukuna/taskit.git
```

### Usage

Run the CLI:
```sh
taskit <command> [<args>]
```

### Commands

- `add <description>`: Add a new task with the given description.
- `list [<status>]`: List all tasks, optionally filtered by status (`to-do`, `in-progress`, `done`).
- `update <id> [<description>] [<status>]`: Update the task with the given id. Optionally update the description and/or status.
- `delete <id>`: Delete the task with the given id.

### Examples

Add a new task:
```sh
taskit add "Buy groceries"
```

List all tasks:
```sh
taskit list
```

List tasks with status `to-do`:
```sh
taskit list to-do
```

Update a task:
```sh
taskit update 1 "Buy groceries and cook dinner" "in-progress"
```

Delete a task:
```sh
taskit delete 1
```
