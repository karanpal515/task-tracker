import sys
from pathlib import Path
import json
from datetime import datetime   

file_path = Path("task_details.json")

# Create the file with an empty list if it doesn't exist
if not file_path.exists() or file_path.stat().st_size == 0:
    with open(file_path, "w") as f:
        json.dump([], f)
args = sys.argv[1:]

if len(args) < 2:
    print("Usage: python task.py add 'Task name'")
    sys.exit(1)

command = args[0].lower()
task_name = args[1]


def connect_with_file(command, task_name=None, task_id=None):

    # Read existing tasks
    with open(file_path, "r") as f:
        data = json.load(f)

    if command == "add":
        new_row = {
            "id": len(data) + 1,
            "description": task_name,
            "status": "todo",
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat()
        }

        data.append(new_row)

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        print("Task added successfully!")

    elif command == "update":
        found = False

        for task in data:
            if task["id"] == int(task_id):
                task["description"] = task_name
                task["updatedAt"] = datetime.now().isoformat()
                found = True
                break

        if found:
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
            print("Task updated successfully!")
        else:
            print("Task not found!")

    elif command == "delete":
        original_length = len(data)

        data = [task for task in data if task["id"] != int(task_id)]

        if len(data) != original_length:
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
            print("Task deleted successfully!")
        else:
            print("Task not found!")

    else:
        print(
            "Invalid action! Use one of: add, update, delete"
        )

connect_with_file(command, task_name)