import sys

def display_menu():
    print("\n" + "=" * 30)
    print("      MY TO-DO LIST APP")
    print("=" * 30)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 30)

def view_tasks(tasks):
    if not tasks:
        print("\n📝 Your to-do list is empty!")
        return
    
    print("\n--- Current Tasks ---")
    # Enumerate gives us a 1-based index for clean user interaction
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['text']}")

def add_task(tasks):
    task_text = input("\nEnter the task description: ").strip()
    if task_text:
        tasks.append({"text": task_text, "completed": False})
        print(f"✨ Added: \"{task_text}\"")
    else:
        print("⚠️ Task cannot be empty!")

def mark_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return
        
    try:
        choice = int(input("\nEnter the number of the task to complete: "))
        # Convert back to 0-based index
        actual_index = choice - 1
        
        if 0 <= actual_index < len(tasks):
            tasks[actual_index]["completed"] = True
            print(f"✅ Marked task #{choice} as completed!")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
        
    try:
        choice = int(input("\nEnter the number of the task to delete: "))
        actual_index = choice - 1
        
        if 0 <= actual_index < len(tasks):
            removed = tasks.pop(actual_index)
            print(f"❌ Deleted: \"{removed['text']}\"")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    # Application state: list of task dictionaries
    tasks = []
    
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("\nGoodbye! Thanks for using the app. 👋")
            sys.exit()
        else:
            print("⚠️ Invalid choice, please pick a number from 1 to 5.")

if __name__ == "__main__":
    main()