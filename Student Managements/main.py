from database.db_connection import create_table
from models.student_class import Student
from services.student_service import *

def menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Show Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    create_table()

    while True:
        menu()
        choice = int(input("Enter choice: "))

        if choice == 1:
            id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")

            student = Student(id, name, age, course)
            add_student(student)

        elif choice == 2:
            get_all_students()

        elif choice == 3:
            id = int(input("Enter ID: "))
            get_student_by_id(id)

        elif choice == 4:
            id = int(input("Enter ID: "))
            name = input("New Name: ")
            age = int(input("New Age: "))
            course = input("New Course: ")

            update_student(id, name, age, course)

        elif choice == 5:
            id = int(input("Enter ID: "))
            delete_student(id)

        elif choice == 6:
            print("👋 Exit")
            break

        else:
            print("❌ Invalid Choice")

if __name__ == "__main__":
    main()