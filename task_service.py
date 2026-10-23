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
    
def view_task():
    tasks=load_task()
    for i in range(len(tasks)):
        print(f"task {i + 1}: {tasks[i]['task']}, Age: {tasks[i]['completed']}")

            
def complete_task():
    tasks=load_task()
    print("\n=== add what you complete ===")
    number= int(input("enter the nuber for the task you complete: "))
    if 1<=number<=len(tasks):
        tasks[number-1]["completed"]=True
        save_task(tasks)
        
        print("Task marked as completed!")
    return None