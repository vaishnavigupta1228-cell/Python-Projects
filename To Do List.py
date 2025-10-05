# todo.py
import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def list_tasks(tasks):
    if not tasks:
        print("No tasks.\n")
        return
    print("\nCurrent tasks:")
    for t in tasks:
        status = "✔" if t.get("done") else " "
        print(f"[{t['id']}] [{status}] {t['title']}")
    print()

def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Empty title — canceled.")
        return
    new_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": new_id, "title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")

def mark_done(tasks):
    try:
        id_ = int(input("Task id to mark done: ").strip())
    except ValueError:
        print("Invalid id.")
        return
    for t in tasks:
        if t["id"] == id_:
            t["done"] = True
            save_tasks(tasks)
            print("Marked done.")
            return
    print("Task not found.")

def delete_task(tasks):
    try:
        id_ = int(input("Task id to delete: ").strip())
    except ValueError:
        print("Invalid id.")
        return
    for i, t in enumerate(tasks):
        if t["id"] == id_:
            ok = input(f"Delete '{t['title']}'? (y/n): ").strip().lower()
            if ok == "y":
                tasks.pop(i)
                save_tasks(tasks)
                print("Deleted.")
            else:
                print("Cancelled.")
            return
    print("Task not found.")

def menu():
    tasks = load_tasks()
    while True:
        print("=== To-Do Menu ===")
        print("1) List tasks")
        print("2) Add task")
        print("3) Mark task as done")
        print("4) Delete task")
        print("5) Quit")
        choice = input("> ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks); tasks = load_tasks()
        elif choice == "3":
            mark_done(tasks); tasks = load_tasks()
        elif choice == "4":
            delete_task(tasks); tasks = load_tasks()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Unknown option. Try again.\n")

if __name__ == "__main__":
    menu()
