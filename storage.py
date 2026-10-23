import json

def load_task():
    try:
        with open("tasks.json","r", encoding="utf-8") as f:
            tasks= json.load(f.read())
        for i in range(len(tasks)):
            print(f"task {i + 1}: {tasks[i]['task']}, Age: {tasks[i]['completed']}")
    except json.JSONDecodeError as error:
        raise ValueError("tasks.json contains invalid JSON.") from error
    
    
def save_task(tasks):
    with open("tasks.json","w", encoding="utf-8") as f:
        json.dump(tasks,f, indent=4, ensure_ascii= False)
        