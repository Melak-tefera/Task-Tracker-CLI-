import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "tasks.json"
def load_task():
    if not DATA_FILE.exists():
        return []
    
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            tasks= json.load(f)
            
        if not isinstance(tasks, list):
            raise ValueError("Task data must be a list.")
        return tasks
    except json.JSONDecodeError as error:
        raise ValueError("tasks.json contains invalid JSON.") from error
    
    
def save_task(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks,f, indent=4, ensure_ascii= False)
        