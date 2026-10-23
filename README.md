# Task Tracker CLI

Task Tracker CLI is a simple Python command-line application for managing daily tasks. Users can add tasks, view all tasks, mark tasks as completed, and save their tasks in a JSON file so the data remains after closing the program.

## Features

- Add a new task
- View all tasks with their status
- Mark a task as completed
- Save tasks automatically to `tasks.json`
- Load saved tasks when the program starts
- Simple menu-based interface
- Basic input validation

## Project Structure

```text
task-tracker/
├── main.py           # Starts the program and shows the menu
├── task_service.py   # Contains task operations
├── storage.py        # Loads and saves tasks using JSON
├── tasks.json        # Stores task data after first use
└── README.md         # Project documentation
```

## Requirements

- Python 3.8 or newer
- No external Python packages are required

## How to Run

1. Open a terminal in the project folder.
2. Run the program:

```bash
python main.py
```

On some systems, you may need to use:

```bash
python3 main.py
```

## How to Use

When the program starts, you will see this menu:

```text
=== TASK TRACKER ===
1. Add task
2. View tasks
3. Complete task
4. Exit
Enter your choice:
```

### Add a Task

Choose `1`, then type the task title.

```text
Enter your choice: 1
Task title: Study Dart
Task added successfully!
```

### View Tasks

Choose `2` to display all saved tasks.

```text
Task 1: Study Dart - Pending
Task 2: Build Flutter app - Completed
```

### Complete a Task

Choose `3`, then enter the number of the task you completed.

```text
Enter the number of the task you completed: 1
Task marked as completed!
```

### Exit

Choose `4` to close the program.

## Data Storage

Tasks are stored in a file called `tasks.json`.

Each task is stored as a dictionary inside a list:

```json
[
    {
        "task": "Study Dart",
        "completed": false
    },
    {
        "task": "Build Flutter app",
        "completed": true
    }
]
```

- `"task"` stores the task title.
- `"completed"` is `false` when the task is pending and `true` when it is completed.
- The program creates `tasks.json` automatically after you add your first task.

## File Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Displays the menu and handles user choices |
| `task_service.py` | Adds, views, and completes tasks |
| `storage.py` | Reads and writes tasks to `tasks.json` |
| `tasks.json` | Stores the task data |

## Error Handling

- Empty task titles are rejected.
- Invalid menu choices show an error message.
- Entering text instead of a number when completing a task is handled safely.
- Invalid task numbers are rejected.
- If `tasks.json` contains invalid JSON, the program raises a clear error message.

## Future Improvements

- Delete tasks
- Edit task titles
- Add task priorities
- Add due dates
- Search tasks
- Show tasks by status: pending or completed
- Add unit tests

## Author

Created by **Melak Tefera** as a Python learning project.