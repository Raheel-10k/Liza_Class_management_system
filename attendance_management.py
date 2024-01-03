class AttendanceManagement:
    def __init__(self, student_data):
        self.student_data = student_data

    def calculate_attendance(self, student_name):
        student = self.get_student_by_name(student_name)
        if student:
            total_days_attended = int(input("Enter total days attended: "))
            total_days_missed = int(input("Enter total days missed: "))
            total_duration = int(input("Enter total duration of the course (in days): "))

            attendance_percentage = (total_days_attended / (total_days_attended + total_days_missed)) * 100
            student['attendance_percentage'] = attendance_percentage

            print(f"\nAttendance Report for {student_name}:")
            print(f"Total Days Attended: {total_days_attended}")
            print(f"Total Days Missed: {total_days_missed}")
            print(f"Total Duration of Course: {total_duration} days")
            print(f"Attendance Percentage: {attendance_percentage:.2f}%")
        else:
            print(f"Student {student_name} not found.")

    def get_student_by_name(self, student_name):
        for student in self.student_data:
            if student['std_name'].lower() == student_name.lower():
                return student
        return None
    
    def calculate_attendance_till_current_date(self, student_name):
        student = self.get_student_by_name(student_name)
        if student:
            total_days_attended = 0
            total_days_missed = 0

            current_date = input("Enter the current date (YYYY-MM-DD): ")

            for attendance_record in student['attendance_data']:
                attendance_date = attendance_record['Date']
                attendance_status = attendance_record['Status']

                # Check if the attendance date is before or equal to the current date
                if attendance_date <= current_date:
                    if attendance_status.lower() == 'present':
                        total_days_attended += 1
                    elif attendance_status.lower() == 'absent':
                        total_days_missed += 1

            total_days = total_days_attended + total_days_missed

            if total_days > 0:
                attendance_percentage = (total_days_attended / total_days) * 100
                print(f"\nAttendance Report for {student_name} till {current_date}:")
                print(f"Total Days Attended: {total_days_attended}")
                print(f"Total Days Missed: {total_days_missed}")
                print(f"Total Days: {total_days}")
                print(f"Attendance Percentage: {attendance_percentage:.2f}%")
            else:
                print("No attendance data available for the student till today.")
        else:
            print(f"Student {student_name} not found.")


if __name__ == "__main__":
    from student_management import StudentManagement

    student_manager = StudentManagement()
    attendance_manager = AttendanceManagement(student_manager.student_data)
    search_name = input("Enter the student name to calculate attendance: ")
    attendance_manager.calculate_attendance(search_name)
