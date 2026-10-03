# Simple To-Do List App
# A beginner Python project: lists, dictionaries, functions, loops and files.

import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Read tasks from the file. If the file doesn't exist yet, start empty."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Write all tasks to the file so they are kept after closing the app."""
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("\nYour list is empty. Add something!\n")
        return
    print("\n--- Your Tasks ---")
    for number, task in enumerate(tasks, start=1):
        mark = "X" if task["done"] else " "
        print(f"{number}. [{mark}] {task['title']}")
    print()


def add_task(tasks):
    title = input("What do you need to do? ").strip()
    if title == "":
        print("Task can't be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")


def pick_task(tasks):
    """Ask the user for a task number and return its index (or None)."""
    show_tasks(tasks)
    if len(tasks) == 0:
        return None
    choice = input("Task number: ")
    if not choice.isdigit() or not (1 <= int(choice) <= len(tasks)):
        print("That's not a valid number.")
        return None
    return int(choice) - 1


def complete_task(tasks):
    index = pick_task(tasks)
    if index is not None:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Nice job! Finished: {tasks[index]['title']}")


def delete_task(tasks):
    index = pick_task(tasks)
    if index is not None:
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}")


def main():
    tasks = load_tasks()
    print("Welcome to your To-Do List!")

    while True:
        print("1) Show tasks")
        print("2) Add task")
        print("3) Mark task as done")
        print("4) Delete task")
        print("5) Quit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please pick a number from 1 to 5.")


if __name__ == "__main__":
    main()
