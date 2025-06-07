task = []

def controls():
    print("To-Do Tasks!")
    view_task()

    try:

        choice = int(input("""\nTo-Do List
1. Add Task
2. Remove Task
3. Quit
Enter Here: """))
        
        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            return choice
        else:
            print("Please enter a number between 1-4")

        
    except ValueError:
        print("Please enter a valid number")

def view_task(filename="task.txt"):
    global task
    try:
        with open(filename, "r") as file:
            task = [line.strip() for line in file]

        if not task:
            print("No tasks.")
        else:
            for number, work in enumerate(task, 1):
                print(f"{number}. {work}")

    except FileNotFoundError:
        print("No saved tasks found.\n")

def add_task():
    work = input("Input a Task: ")
    task.append(work)
    print("\nAdding task ....")
    save()
    print("\nTask Added!\n")

def remove_task():
    task_number = int(input("Enter the task number you want to remove: "))
    task.pop(task_number-1)
    print("\nRemoving task ....")
    save()
    print("\nTask Removed!\n")

def save(filename="task.txt"):
    with open(filename, "w") as file:
        for work in task:
            file.write(work +"\n")

while True:
    if controls() == 3:
        print("\nThank for using To-Do List")
        break