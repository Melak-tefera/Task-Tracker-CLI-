from storage import load_task, save_task

def add_task(title):
    title= title.strip()
    tasks = load_task()
    task={
        "task":title,
        "completed": False
    }
    tasks.append(task)
    save_task(tasks)
    print("Task added successfully!")
    return task
    
def view_task():
    return load_task()
            
def complete_task():
    tasks=load_task()
    print("\n=== add what you complete ===")
    number= int(input("enter the nuber for the task you complete: "))
    if 1<=number<=len(tasks):
        tasks[number-1]["completed"]=True
        print("Task marked as completed!")
    return None