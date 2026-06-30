# Project URL 
https://github.com/karanpal515/task-tracker
Project URL: https://roadmap.sh/projects/task-tracker
# Task Tracker CLI

A simple command-line task tracker application built with Python. This project allows you to manage your tasks directly from the terminal using JSON file storage.

## Features

* Add a new task
* Update an existing task
* Delete a task
* Store tasks in a JSON file
* Automatically track creation and update timestamps

## Project Structure

```text
task_tracker/
│
├── add_task.py
├── task_details.json
└── README.md
```

## Requirements

* Python 3.8 or higher

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd task_tracker
```

No external packages are required.

## Usage

### Add a Task

```bash
python add_task.py add "Buy groceries"
```

Example output:

```text
Task added successfully!
```

---

### Update a Task

```bash
python add_task.py update 1 "Buy milk"
```

Example output:

```text
Task updated successfully!
```

---

### Delete a Task

```bash
python add_task.py delete 1
```

Example output:

```text
Task deleted successfully!
```

---

## Task Storage Format

Tasks are stored in `task_details.json` as JSON objects:

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": "2026-06-30T20:30:15.123456",
        "updatedAt": "2026-06-30T20:30:15.123456"
    }
]
```

## Available Commands

| Command  | Description             |
| -------- | ----------------------- |
| `add`    | Add a new task          |
| `update` | Update an existing task |
| `delete` | Delete a task           |

## Error Handling

The application handles:

* Missing command-line arguments
* Invalid commands
* Empty JSON files
* Non-existent task IDs
