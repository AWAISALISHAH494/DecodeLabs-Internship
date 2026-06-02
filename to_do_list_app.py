import json
import os

TODO_FILE = 'todo.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    task = input("\nEnter a new task: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet! Add some tasks.")
        return
    
    print("\n" + "="*50)
    print("YOUR TO-DO LIST")
    print("="*50)
    for i, task in enumerate(tasks, 1):
        status = "DONE" if task["completed"] else "PENDING"
        print(f"{i:2d}. {status} {task['task']}")
    print("="*50)

def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to mark as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number!")
    except:
        print("Please enter a valid number!")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num-1)
            print(f"Deleted: {deleted['task']}")
        else:
            print("Invalid task number!")
    except:
        print("Please enter a valid number!")

def main():
    tasks = load_tasks()
    print("Welcome to Your To-Do List")

    while True:
        print("\n" + "-"*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Complete")
        print("4. Delete Task")
        print("5. Exit")
        print("-"*40)
        
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()