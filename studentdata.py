students = {}
def add_student():
    try:
        roll = int(input("Enter Roll Number: "))
        if roll in students:
            print("Roll Number already exists!")
            return
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = tuple(map(int, input("Enter 3 subject marks separated by space: ").split()))
        if len(marks) != 3:
            print("Enter exactly 3 marks!")
            return
        section = input("Enter Section: ")
        students[roll] = {"Name": name, "Age": age, "Marks": marks, "Section": section}
        print("Student added successfully!")
    except ValueError:
        print("Invalid input!")

def display_students():
    if not students:
        print("No records found.")
    else:
        for roll, d in students.items():
            print(f"Roll: {roll}, Name: {d['Name']}, Age: {d['Age']}, Marks: {d['Marks']}, Section: {d['Section']}")

def search_student():
    try:
        roll = int(input("Enter Roll Number to search: "))
        d = students.get(roll)
        print(f"Found -> Roll: {roll}, Name: {d['Name']}, Age: {d['Age']}, Marks: {d['Marks']}, Section: {d['Section']}" if d else "Student not found.")
    except ValueError:
        print("Invalid input!")

def remove_student():
    try:
        roll = int(input("Enter Roll Number to remove: "))
        removed = students.pop(roll, None)
        print(f"Removed -> {removed}" if removed else "Student not found.")
    except ValueError:
        print("Invalid input!")

def show_topper():
    if students:
        roll, d = max(students.items(), key=lambda x: sum(x[1]["Marks"]))
        print(f"Topper -> Roll: {roll}, Name: {d['Name']}, Total Marks: {sum(d['Marks'])}")
    else:
        print("No records found.")

def show_sections():
    sections = {d["Section"] for d in students.values()}
    print("Unique Sections:", sections if sections else "No sections found.")

while True:
    print("\nSchool Data Management System")
    print("1. Add Student\n2. Display All Students\n3. Search Student\n4. Remove Student\n5. Show Topper\n6. Show Sections\n7. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice == 1: add_student()
        elif choice == 2: display_students()
        elif choice == 3: search_student()
        elif choice == 4: remove_student()
        elif choice == 5: show_topper()
        elif choice == 6: show_sections()
        elif choice == 7: break
        else: print("Invalid choice!")
    except ValueError:
        print("Enter a number between 1-7.")