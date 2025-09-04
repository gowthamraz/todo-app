import os
import json

FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

# Show all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n📌 No tasks yet.")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, 1):
            status = "✅ Done" if task["done"] else "⏳ Pending"
            print(f"{i}. {task['task']} [{status}]")

# Add a task
def add_task(tasks):
    task_name = input("Enter new task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print(f"✅ '{task_name}' added!")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"❌ '{removed['task']}' removed!")
        except (ValueError, IndexError):
            print("Invalid number.")

# Mark task as done
def mark_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as done: "))
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print(f"✅ '{tasks[task_num - 1]['task']}' marked as done!")
        except (ValueError, IndexError):
            print("Invalid number.")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
