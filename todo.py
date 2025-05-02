import os

tasks = []

# Load saved tasks if file exists
if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r", encoding="utf-8") as f:
        tasks = [line.strip() for line in f.readlines()]

while True:
    print("\n--- MENU ---")
    print("1. Add task")
    print("2. Remove task")
    print("3. View all tasks")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == "2":
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        to_remove = int(input("Enter the task number to remove: ")) - 1
        if 0 <= to_remove < len(tasks):
            removed = tasks.pop(to_remove)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")

    elif choice == "3":
        if not tasks:
            print("No tasks.")
        else:
            print("\n--- Task List ---")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    elif choice == "4":
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")
        print("Saved. Goodbye!")
        break

    else:
        print("Invalid option.")