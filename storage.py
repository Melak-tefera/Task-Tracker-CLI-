import json

def load_task():
    try:
        with open("tasks.json","r", encoding="utf-8") as f:
            tasks= json.loads(f.read())
        return tasks
        
    except json.JSONDecodeError as error:
        raise ValueError("tasks.json contains invalid JSON.") from error
    
    
def save_task(tasks):
    with open("tasks.json","w", encoding="utf-8") as f:
        json.dump(tasks,f, indent=4, ensure_ascii= False)
        