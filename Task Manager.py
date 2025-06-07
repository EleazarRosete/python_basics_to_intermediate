tasks = []

class Task:
    def __init__(self, title, description, done=False):
        self.title = title
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True

    def status(self):
        return "Done" if self.done else "Not yet"

    def edit_task(self, new_title, new_description):
        self.title = new_title
        self.description = new_description

    def __str__(self):
        return f"{self.title}: {self.description} - {self.status()}"

# --- Functions for Task Management ---
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append(Task(title, description))
    print("Task added!\n")

def view_tasks():
    if not tasks:
        print("No tasks yet.\n")
        return
    print("\n--- Task List ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def edit_task():
    view_tasks()
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("New title: ")
            new_description = input("New description: ")
            tasks[index].edit_task(new_title, new_description)
            print("Task updated!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input.\n")

def complete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index].mark_done()
            print("Task marked as done!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input.\n")

def menu():
    while True:
        print("Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

# --- Run the Task Manager ---
menu()
