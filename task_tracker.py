tasks=[]
def add_task():
    title= input("enter title input:  ").strip()
    task={
        "task":title,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    
def view_task():
    if not tasks:
        print("on tasks yet")
        return
    else:
        for x in tasks:
            print(f" {x["task"]}, {x["completed"]}")
            
def complete_task():
    view_task()
    print("\n=== add what you complete ===")
    number= int(input("enter the nuber for the task you complete: "))
    if 1<=number<=len(tasks):
        tasks[number-1]["completed"]=True
        print("Task marked as completed!")
def main_list():
    while True:
        print("\n=== TASK TRACKER ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit")
        choice= input("enter your chice:").strip()
        if choice=="1":
            add_task()
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