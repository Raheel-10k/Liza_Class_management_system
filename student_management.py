import random

class StudentManagement:
    def __init__(self):
        self.student_data = [
            {'uid': 1232, 'std_name': 'john doe', 'email': 'example@gmail.com', 'course_selected': 'BTech CSE',
             'passing_year': 2027, 'starting_year': 2023, 'current_year': 2023},
            {'uid': 1215, 'std_name': 'jane doe', 'email': 'example1@gmail.com', 'course_selected': 'BTech CSE',
             'passing_year': 2027, 'starting_year': 2023, 'current_year': 2026}
        ]

    def get_student_by_name(self, student_name):
        for student in self.student_data:
            if student['std_name'].lower() == student_name.lower():
                return student
        return None

    def add_new_student(self, student_name):
        unique_id = self.generate_unique_id()
        email = input("Enter student email: ")
        allowed_courses = ['BTech CSE', 'Civil Engineering', 'Mechanical Engineering', 'Electrical Engineering']
        while True:
            course_selected = input(f"Enter course selected ({', '.join(allowed_courses)}): ")
            if course_selected in allowed_courses:
                break
            else:
                print("Invalid course selection. Please choose from the allowed courses.")

        passing_year = int(input("Enter passing year: "))
        starting_year = int(input("Enter starting year: "))
        current_year = int(input("Enter current year: "))

        new_student = {
            'uid': unique_id,
            'std_name': student_name,
            'email': email,
            'course_selected': course_selected,
            'passing_year': passing_year,
            'starting_year': starting_year,
            'current_year': current_year
        }

        self.student_data.append(new_student)
        print(f"New student {student_name} added successfully.")

    def delete_student(self, uid, student_name):
        confirmation_uid = int(input("To confirm deletion, re-enter the UID: "))
        if confirmation_uid == uid:
            for student in self.student_data:
                if student['uid'] == uid and student['std_name'].lower() == student_name.lower():
                    self.student_data.remove(student)
                    print(f"Student {student_name} with UID {uid} deleted successfully.")
                    break
            else:
                print("Student not found. Deletion unsuccessful.")
        else:
            print("UID confirmation failed. Deletion unsuccessful.")

    def generate_unique_id(self):
        while True:
            unique_id = random.randint(1000, 9999)
            if all(student['uid'] != unique_id for student in self.student_data):
                return unique_id


if __name__ == "__main__":
    student_manager = StudentManagement()

    # while block can be directly implemented in the main.py file, else use different logic for same task
    while True:
        search_name = input("Enter the student name to search: ")
        existing_student = student_manager.get_student_by_name(search_name)

        if existing_student:
            print(f"Student found: {existing_student}")
            break
        else:
            print(f"Student {search_name} not found.")

            add_option = input("Do you want to add this student? (yes/no): ")
            if add_option.lower() == 'yes':
                student_manager.add_new_student(search_name)
                break


    uid_to_delete = 1234  #ask in main.py as user input
    name_to_delete = "John Doe"     #ask in main.py as user input
    student_manager.delete_student(uid_to_delete, name_to_delete)


    print("\nUpdated Student Data:")        #ask user again if he wishes to print it or not.
    for student in student_manager.student_data:
        print(student)