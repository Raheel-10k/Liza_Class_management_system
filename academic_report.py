class AcademicReport:
    def __init__(self, student_data):
        self.student_data = student_data

    def generate_academic_report(self, student_name):
        student = self.get_student_by_name(student_name)
        if student:
            attendance_percentage = student['attendance_percentage']
            marks_obtained = float(input("Enter marks obtained: "))
            academic_performance = self.evaluate_academic_performance(attendance_percentage, marks_obtained)

            print(f"\nAcademic Report for {student_name}:")
            print(f"Attendance Percentage: {attendance_percentage:.2f}%")
            print(f"Marks Obtained: {marks_obtained}")
            print(f"Academic Performance: {academic_performance}")
        else:
            print(f"Student {student_name} not found.")

    def evaluate_academic_performance(self, attendance_percentage, marks_obtained):
        # Change ASK H
        if attendance_percentage >= 80 and marks_obtained >= 70:
            return "Excellent"
        elif attendance_percentage >= 70 and marks_obtained >= 60:
            return "Good"
        elif attendance_percentage >= 60 and marks_obtained >= 50:
            return "Satisfactory"
        else:
            return "Needs Improvement"

    def get_student_by_name(self, student_name):
        for student in self.student_data:
            if student['std_name'].lower() == student_name.lower():
                return student
        return None
