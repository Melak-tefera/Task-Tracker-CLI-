# Task-Tracker-CLI-
# Task Tracker

A simple Python command-line application for managing daily tasks. Users can add tasks, view tasks, and mark tasks as completed.

## Features

- Add a new task
- View all tasks
- Mark a task as completed
- Automatically number tasks
- Simple menu-based interface
- Runs until the user chooses to exit

## Requirements

- Python 3

Check your Python version:

```bash
python --version
```

## How to Run

1. Save the program as `task_tracker.py`.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python task_tracker.py
```

Or:

```bash
python3 task_tracker.py
```

## Menu Options

```text
=== TASK TRACKER ===
1. Add task
2. View tasks
3. Complete task
4. Exit
```

### 1. Add Task

Allows the user to enter a new task.

Example:

```text
Enter title input: Study Python
Task added successfully!
```

### 2. View Tasks

Displays all tasks with their completion status.

Example:

```text
1. Study Python, False
2. Buy shoes, True
```

- `False` means the task is pending.
- `True` means the task is completed.

### 3. Complete Task

Displays all tasks and asks the user to enter the number of the completed task.

Example:

```text
Enter the number for the task you complete: 1
Task marked as completed!
```

### 4. Exit

Closes the program.

```text
Goodbye!
```

## How Tasks Are Stored

Tasks are stored in a Python list.

```python
tasks = []
```

Each task is a dictionary:

```python
task = {
    "task": "Study Python",
    "completed": False
}
```

Example task list:

```python
tasks = [
    {
        "task": "Study Python",
        "completed": False
    },
    {
        "task": "Buy shoes",
        "completed": True
    }
]
```

## Main Functions

### `add_task()`

Adds a new task to the task list.

```python
def add_task():
    title = input("Enter title input: ").strip()

    task = {
        "task": title,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")
```

### `view_task()`

Displays all tasks.

```python
def view_task():
    if not tasks:
        print("No tasks yet.")
        return

    for x in tasks:
        print(f"{x['task']}, {x['completed']}")
```

### `complete_task()`

Marks a selected task as completed.

```python
def complete_task():
    view_task()

    number = int(input("Enter the number for the task you complete: "))

    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        print("Task marked as completed!")
```

### `main_list()`

Displays the main menu and controls the program flow.

```python
def main_list():
    while True:
        print("\n=== TASK TRACKER ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-4.")
```

## Program Entry Point

```python
if __name__ == "__main__":
    main_list()
```

This starts the program only when `task_tracker.py` is run directly.

## Example Usage

```text
=== TASK TRACKER ===
1. Add task
2. View tasks
3. Complete task
4. Exit
Enter your choice: 1
Enter title input: Study Flutter
Task added successfully!

=== TASK TRACKER ===
1. Add task
2. View tasks
3. Complete task
4. Exit
Enter your choice: 2
1. Study Flutter, False

=== TASK TRACKER ===
1. Add task
2. View tasks
3. Complete task
4. Exit
Enter your choice: 3
1. Study Flutter, False

=== add what you complete ===
Enter the number for the task you complete: 1
Task marked as completed!
```

## Limitations

- Tasks are not saved permanently.
- Tasks disappear when the program closes.
- There is no delete task option.
- Invalid task numbers are not fully handled.
- Task status is shown as `True` or `False`.

## Future Improvements

- Save tasks to a JSON file
- Load tasks when the program starts
- Add a delete task option
- Add task deadlines
- Add task priorities
- Show `Pending` and `Completed` instead of `False` and `True`
- Add error handling with `try` and `except`

## License

This project is created for learning purposes.