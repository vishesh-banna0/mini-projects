import json

FILE_NAME = "todo_list.json"


def load_task():
    """Loads tasks from the JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tasks": []}
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return {"tasks": []}


def save_task(tasks):
    """Saves tasks to the JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Failed to save tasks: {e}")


def view_task(tasks):
    """Displays the list of tasks."""
    print("\nYour To-Do List:")
    tasks_list = tasks["tasks"]
    if not tasks_list:
        print("  - No tasks available.")
    else:
        for idx, task in enumerate(tasks_list, start=1):
            status = "[Completed]" if task["complete"] else "[Incomplete]"
            print(f"  {idx}. {task['description']} {status}")


def create_task(tasks):
    """Adds a new task to the list."""
    description = input("Enter Task Description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_task(tasks)
        print("✅ Task Created!")
    else:
        print("❌ Description cannot be empty.")


def mark_task_complete(tasks):
    """Marks a task as complete."""
    view_task(tasks)
    try:
        task_number = int(input("Enter the Task No. to mark as completed: "))
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_task(tasks)
            print("✅ Task marked as Completed!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")


def delete_task(tasks):
    """Deletes a task from the list."""
    view_task(tasks)
    try:
        del_number = int(input("Enter the Task No. to delete: "))
        if 1 <= del_number <= len(tasks["tasks"]):
            del tasks["tasks"][del_number - 1]
            save_task(tasks)
            print("✅ Task Deleted!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the To-Do List Manager."""
    tasks = load_task()
    while True:
        print("\n📌 To-Do List Manager")
        print("1️⃣ View Tasks")
        print("2️⃣ Add Task")
        print("3️⃣ Mark Task as Complete")
        print("4️⃣ Delete Task")
        print("5️⃣ Exit")

        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid Choice. Please try again.")


if __name__ == "__main__":
    main()
