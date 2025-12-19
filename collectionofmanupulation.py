students = []
subjects = set()

while True:
    print("\n-- Student Detail --")
    print("1. Add student")
    print("2. Display all students")
    print("3. Update student age")
    print("4. Delete student")
    print("5. Display subjects")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            id = int(input("Enter id: "))
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            dob = input("Enter date of birth (YYYY-mm-dd): ")
            sub = input("Enter subjects (comma separated): ")

            sub_list = sub.split(",")

            for s in sub_list:
                subjects.add(s.strip())

            student = {
                "id": id,
                "dob": dob,
                "name": name,
                "age": age,
                "grade": grade,
                "subject": sub_list
            }

            students.append(student)
            print("Student added successfully")

        case 2:
            if not students:
                print("No student records found")
            else:
                for s in students:
                    print(
                       f"Student Id: {id} | "
                       f"Name: {name} | "
                       f"Age: {age} | "
                       f"Grade: {grade} | "
                       f"Date of Birth (yyyy/mm/dd): {dob} | "
                        f"Subjects: {', '.join(s['subject'])} "
                         )

        case 3:
            id = int(input("Enter student id: "))
            found = False

            for s in students:
                if s["id"] == id:
                    s["age"] = int(input("Enter new age: "))
                    print("Age updated")
                    found = True
                    break

            if not found:
                print("Student not found")

        case 4:
            id = int(input("Enter student id: "))
            found = False

            for s in students:
                if s["id"] == id:
                    students.remove(s)
                    print("Student deleted")
                    found = True
                    break

            if not found:
                print("Student not found")

        case 5:
          if not subjects:
           print("No subjects added yet.")
          else:
           print("\n| Subjects Offered |")
          for i, sub in enumerate(sorted(subjects), 1):
            print(f"{i}. {sub}")
            
        case 6:
            print("Thank you!")
            break

        case _:
            print("Invalid choice")
