students = {}

def load(filename="student.txt"):
    try:
        with open(filename, 'r') as file:
            current_student = None
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if ":" not in line:
                    current_student = line
                    students[current_student] = {}
                else:
                    subject, grade = line.split(":")
                    students[current_student][subject.strip()] = int(grade.strip())
        print("Data loaded successfully.\n")
    except FileNotFoundError:
        print("No saved file found. Starting with empty data.\n")

def save(filename="student.txt"):
    with open(filename, 'w') as file:
        for student, grades in students.items():
            file.write(student + "\n")
            for subject, grade in grades.items():
                file.write(f"{subject}:{grade}\n")

def add_student():
    name = input("Enter the name of the student: ").strip()
    if name in students:
        print("Student already exists.")
    else:
        students[name] = {
            "Math": 0,
            "English": 0,
            "Filipino": 0,
            "MAPEH": 0,
            "Science": 0,
            "History": 0
        }
        print(f"{name} has been added.")

def remove_student():
    name = input("Enter the name of the student to remove: ").strip()
    if name in students:
        del students[name]
        print(f"{name} has been removed.")
    else:
        print("Student not found.")

def edit_grade(name):
    if name not in students:
        print("Student not found.")
        return
    subject = input("Enter subject to edit: ").strip()
    if subject not in students[name]:
        print("Subject not found.")
        return
    try:
        value = int(input("Enter new grade: "))
        students[name][subject] = value
        print("Grade updated.")
    except ValueError:
        print("Please enter a valid number.")

def add_grade(name):
    if name not in students:
        print("Student not found.")
        return
    subject = input("Enter subject to add or update: ").strip()
    try:
        value = int(input("Enter grade: "))
        students[name][subject] = value
        print("Grade added/updated.")
    except ValueError:
        print("Please enter a valid number.")

def avg_per_student():
    for student, grades in students.items():
        average = sum(grades.values()) / len(grades)
        print(f"{student}'s average grade is: {average:.2f}")

def avg_per_subject():
    subject = input("Enter subject to calculate average: ").strip()
    total = 0
    count = 0
    for student in students:
        if subject in students[student]:
            total += students[student][subject]
            count += 1
        else:
            print(f"{student} has no grade for {subject}")
    if count:
        print(f"\nAverage grade for {subject}: {total / count:.2f}")
    else:
        print("No students have that subject.")

def view_students():
    if not students:
        print("No students to show.")
        return
    print("\nList of Students:")
    for i, student in enumerate(students, 1):
        print(f"{i}. {student}")

def view_grade(name):
    grades = students.get(name)
    if not grades:
        print("Student not found.")
        return
    print(f"\n{name}'s Grades:")
    total = 0
    for subject, grade in grades.items():
        print(f"{subject:<10}: {grade}")
        total += grade
    average = total / len(grades)
    print(f"\nAverage   : {average:.2f}")

def controls():
    while True:
        print("\n--- Student Grading System ---")
        print("1. View Students")
        print("2. View Student Grades")
        print("3. Add Student")
        print("4. Edit Student Grade")
        print("5. Add/Update Grade")
        print("6. Remove Student")
        print("7. Average per Student")
        print("8. Average per Subject")
        print("9. Save")
        print("0. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_students()
            elif choice == 2:
                name = input("Enter student name: ")
                view_grade(name)
            elif choice == 3:
                add_student()
            elif choice == 4:
                name = input("Enter student name: ")
                edit_grade(name)
            elif choice == 5:
                name = input("Enter student name: ")
                add_grade(name)
            elif choice == 6:
                remove_student()
            elif choice == 7:
                avg_per_student()
            elif choice == 8:
                avg_per_subject()
            elif choice == 9:
                save()
                print("Data saved.")
            elif choice == 0:
                print("Exiting...")
                save()
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Start the program
load()
controls()
