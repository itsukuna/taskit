# Taskit

[Project](https://roadmap.sh/projects/task-tracker/solutions?u=647426d9c4ec366ad5b0f25a) from Roadmap.sh

## Prerequisites

- Python 3.10+
- [pipx](https://pypa.github.io/pipx/)

### Installation

```sh
pipx install git+https://github.com/itsukuna/taskit.git
```

If you don't have `pipx` installed, you can install it first:

```sh
python3 -m pip install --user pipx
python3 -m pipx ensurepath
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
