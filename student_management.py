# List of students stored as tuples (Student ID, Name, Age)
students = [
    (101, "Alice", 20),
    (102, "Bob", 22),
    (103, "Charlie", 21),
]

# Set of courses (ensures unique course names)
courses = {"Math", "Physics", "Computer Science"}

# Dictionary to store enrolled courses for each student (ID → Set of courses)
enrollments = {
    101: {"Math", "Physics"},
    102: {"Computer Science"},
    103: {"Math", "Computer Science"},
}

while True:
    print("\n1. Display Students")
    print("2. Display Courses")
    print("3. Enroll Student in a Course")
    print("4. View Student Enrollments")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  # Display all students
        print("\nStudents:")
        print("-----------------")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}")
        print("-----------------\n")

    elif choice == "2":  # Display available courses
        print("\nAvailable Courses:")
        print("-----------------")
        for course in courses:
            print(course)
        print("-----------------\n")

    elif choice == "3":  # Enroll a student in a course
        student_id = input("Enter Student ID: ")
        course_name = input("Enter Course Name: ")

        if student_id.isdigit():
            student_id = int(student_id)
            if student_id in [s[0] for s in students]:  # Check if student exists
                if course_name in courses:  # Check if course exists
                    if student_id in enrollments:
                        enrollments[student_id].add(course_name)
                    else:
                        enrollments[student_id] = {course_name}
                    print("\nStudent Enrolled Successfully!\n")
                else:
                    print("\nInvalid Course Name!\n")
            else:
                print("\nStudent Not Found!\n")
        else:
            print("\nInvalid Input! Student ID must be a number.\n")

    elif choice == "4":  # View student enrollments
        student_id = input("Enter Student ID: ")

        if student_id.isdigit():
            student_id = int(student_id)
            if student_id in enrollments:
                print(f"\nCourses Enrolled by Student {student_id}: {', '.join(enrollments[student_id])}\n")
            else:
                print("\nNo Enrollments Found for This Student!\n")
        else:
            print("\nInvalid Input! Student ID must be a number.\n")

    elif choice == "5":  # Exit the program
        print("Exiting Program...")
        break

    else:
        print("\nInvalid Choice! Try Again.\n")
