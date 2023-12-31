from student_management import StudentManagement
from attendance_management import AttendanceManagement
from academic_report import AcademicReport
from course_management import CourseManagement
from lisa import LoginSystem

def display_menu():
    print("\nSelect a Task:")
    print("1. Register")
    print("2. Student Profile")
    print("3. Eligibility Criteria")
    print("4. Course Details")
    print("5. Overall Attendance")
    print("6. Attendance till Current Date")
    print("7. Get Your Academic Report")
    print("8. Exit")

if __name__ == "__main__":
    student_manager = StudentManagement()
    attendance_manager = AttendanceManagement(student_manager.student_data)
    academic_report_generator = AcademicReport(student_manager.student_data)
    course_manager = CourseManagement(student_manager)
    login_system = LoginSystem(student_manager)

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            login_system.register_user()
        elif choice == "2":
            student_name = input("Enter the student name to view profile: ")
            student = student_manager.get_student_by_name(student_name)
            if student:
                print(f"Student Profile:\n{student}")
            else:
                print(f"Student {student_name} not found.")
        elif choice == "3":
            
            student_name = input("Enter the student name to check eligibility criteria: ")
            student = student_manager.get_student_by_name(student_name)

            if student:
                physics_marks = float(input(f"Enter {student_name}'s marks in Physics: "))
                chemistry_marks = float(input(f"Enter {student_name}'s marks in Chemistry: "))
                math_marks = float(input(f"Enter {student_name}'s marks in Math: "))

                percentage = (physics_marks + chemistry_marks + math_marks) / 3

                if percentage >= 50:
                    print(f"{student_name} is eligible with {percentage}%.")
                else:
                    print(f"{student_name} is not eligible. Minimum 50% required, but has {percentage}%.")
            else:
                register_choice = input(f"Student {student_name} not found. Do you want to register? (yes/no): ").lower()
                if register_choice == "yes":
                    login_system.register_user()
                else:
                    print("Returning to the main menu.")

        elif choice == "4":
            student_name = input("Enter the student name to select a specialization: ")
            student = student_manager.get_student_by_name(student_name)
            if student:
                course_manager.select_specialization(student)
            else:
                print(f"Student {student_name} not found.")
        elif choice == "5":
            student_name = input("Enter the student name to calculate overall attendance: ")
            attendance_manager.calculate_attendance(student_name)
        elif choice == "6":
            student_name = input("Enter the student name to calculate attendance till today: ")
            attendance_manager.calculate_attendance_till_current_date(student_name)

        elif choice == "7":
            student_name = input("Enter the student name to generate the academic report: ")
            academic_report_generator.generate_academic_report(student_name)
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
