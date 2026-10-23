from task_service import add_task, view_task, complete_task
from storage import load_task, save_task

def main_list():
    while True:
        print("\n=== TASK TRACKER ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit")
        choice= input("enter your chice:").strip()
        if choice=="1":
            title = input("Task title: ")
            task=add_task(title)
            print(f'Task added: {task["task"]}')
            
        elif choice=="2":
            view_task()
        elif choice=="3":
            complete_task()
        elif choice=="4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-4.")

if __name__ == "__main__":
    main_list()