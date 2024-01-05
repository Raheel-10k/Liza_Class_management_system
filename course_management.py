class CourseManagement:
    def _init_(self, student_manager):
        self.student_manager = student_manager
        self.specialization_options = {
            'BTech CSE': ['Machine Learning', 'Network Security', 'Data Science'],
            'Electrical Engineering': ['Control systems', 'Communication and Signal Processing System', 'Power Systems'],
            'Mechanical Engineering': ['Biomedical and Engineering Fluid Mechanics', 'Combustion and the Environment', 'Mechanical Design'],
            'Civil Engineering': ['Materials Engineering', 'Construction Engineering', 'Transportation Engineering', 'Structural Engineering', 'Geotechnical Engineering']

        }

    def select_specialization(self, student):
        course_selected = student['course_selected']
        if student['current_year'] - 3 == student['starting_year']:
            valid_specializations = self.specialization_options.get(course_selected, [])
            
            while True:
                print(f"Specialization options for {course_selected}: {', '.join(valid_specializations)}")
                specialization = input("Select a specialization: ")

                if specialization in valid_specializations:
                    student['specialization_course'] = specialization
                    print(f"Specialization course {specialization} selected for {student['std_name']}.")
                    break
                else:
                    print(f"Invalid specialization. Please select from the available options.")