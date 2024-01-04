import matplotlib.pyplot as plt
from datetime import datetime

class StudentManagement:
    @staticmethod
    def email_exists(email):
        return False

class Login:
    class User:
        def __init__(self, username, password, field):
            self.username = username
            self.password = password
            self.field = field
            self.subjects = []
            self.online_lectures = []
            self.attendance_data = []

class LoginSystem:
    def __init__(self):
        self.users = []

    def register_user(self):
        email = input("Enter your email: ")

        if any(user.username == email.split('@')[0] for user in self.users):
            print("Email already exists. Please use a different email.")
            return

        password = input("Enter a password: ")
        username = email.split('@')[0]

        print("Select your field:")
        print("1. BTech CSE")
        print("2. Electrical Engineering")
        print("3. Civil Engineering")
        print("4. Mechanical Engineering")

        field_choice = input("Enter the number corresponding to your field (1-4): ")

        if field_choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please choose a valid field.")
            return

        fields = ['BTech CSE', 'Electrical Engineering', 'Civil Engineering', 'Mechanical Engineering']
        selected_field = fields[int(field_choice) - 1]

        if selected_field == 'BTech CSE':
            subjects = ['Programming', 'Data Structures', 'Algorithms', 'Database Management']
        elif selected_field == 'Electrical Engineering':
            subjects = ['Circuits', 'Electronics', 'Power Systems', 'Control Systems']
        elif selected_field == 'Civil Engineering':
            subjects = ['Structural Analysis', 'Concrete Technology', 'Fluid Mechanics', 'Transportation Engineering']
        elif selected_field == 'Mechanical Engineering':
            subjects = ['Thermodynamics', 'Mechanics of Materials', 'Fluid Mechanics', 'Machine Design']
        else:
            subjects = []

        new_user = Login.User(username, password, selected_field)
        new_user.subjects = subjects
        self.users.append(new_user)
        print(f"User {username} registered successfully with the field: {selected_field}.")
        self.show_user_options(new_user)

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        username = email.split('@')[0]

        user = next((user for user in self.users if user.username == username and user.password == password), None)

        if user:
            print(f"Welcome, {username}! Login successful.")
            self.show_user_options(user)
            return True
        else:
            print("Invalid email or password. Please try again.")
            return False

    def show_user_options(self, user):
        while True:
            print("\nOptions:")
            print("1. View Profile")
            print("2. View Subjects")
            print("3. View Online Lectures")
            print("4. Mark Attendance")
            print("5. View Attendance Data")
            print("6. Logout")
            print("7. Plot Attendance Graph")

            choice = input("Enter your choice (1-7): ")

            if choice == '1':
                self.view_profile(user)
            elif choice == '2':
                self.view_subjects(user)
            elif choice == '3':
                self.view_online_lectures(user)
            elif choice == '4':
                self.mark_attendance(user)
            elif choice == '5':
                self.view_attendance_data(user)
            elif choice == '6':
                print("Logout successful.")
                break
            elif choice == '7':
                self.plot_attendance_graph(user)
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

    def view_profile(self, user):
        print(f"\nProfile for {user.username}:")
        print(f"Field: {user.field}")

    def view_subjects(self, user):
        print(f"\nSubjects for {user.username} in {user.field}:")
        for subject in user.subjects:
            print(subject)

    def view_online_lectures(self, user):
        print(f"\nOnline Lectures for {user.username} in {user.field}:")

        schedule = [
            {'Time': '10:30 AM - 12:00 PM', 'Subject': 'Programming'},
            {'Time': '1:00 PM - 2:30 PM', 'Subject': 'Data Structures'},
            {'Time': '3:00 PM - 4:30 PM', 'Subject': 'Algorithms'},
            {'Time': '5:00 PM - 6:30 PM', 'Subject': 'Database Management'},
        ]

        for lecture in schedule:
            print(f"{lecture['Time']} - {lecture['Subject']}")

    def mark_attendance(self, user):
        print("\nMark Attendance:")
        print("Select the class to mark attendance:")
        for index, subject in enumerate(user.subjects, start=1):
            print(f"{index}. {subject}")

        subject_choice = input("Enter the number corresponding to the class (1-4): ")

        try:
            subject_index = int(subject_choice) - 1
            selected_subject = user.subjects[subject_index]
        except (ValueError, IndexError):
            print("Invalid choice. Please choose a valid class.")
            return

        date = input("Enter the date (YYYY-MM-DD): ")

        # Check if attendance has already been marked for the selected lecture on the given date
        if any(record['Subject'] == selected_subject and record['Date'] == date for record in user.attendance_data):
            print(f"Attendance for {selected_subject} on {date} has already been marked.")
        else:
            attendance_status = input("Attendance (Present/Absent): ")
            user.attendance_data.append({
                'Date': date,
                'Subject': selected_subject,
                'Status': attendance_status,
            })
            print(f"Attendance marked for {selected_subject} on {date}.")

    def view_attendance_data(self, user):
        print("\nAttendance Data:")
        for attendance_record in user.attendance_data:
            print(f"Date: {attendance_record['Date']}, Subject: {attendance_record['Subject']}, Status: {attendance_record['Status']}")

    def plot_attendance_graph(self, user):
        if not user.attendance_data:
            print("No attendance data available to plot.")
            return

        subjects = set(record['Subject'] for record in user.attendance_data)
        dates = sorted(set(record['Date'] for record in user.attendance_data))
        
        # Create a dictionary to store attendance counts for each subject on each date
        attendance_counts = {subject: [0] * len(dates) for subject in subjects}

        # Fill in the attendance counts
        for record in user.attendance_data:
            subject = record['Subject']
            date = record['Date']
            index = dates.index(date)
            attendance_counts[subject][index] += 1

        # Plotting the attendance graph
        plt.figure(figsize=(10, 6))
        for subject in subjects:
            plt.plot(dates, attendance_counts[subject], label=subject, marker='o')

        plt.title(f"Attendance Graph for {user.username}")
        plt.xlabel("Date")
        plt.ylabel("Attendance Count")
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()

        # Show the plot
        plt.show()


login_system = LoginSystem()

login_system.register_user()

login_system.login()

# Uncomment the line below to test plotting the attendance graph
# login_system.plot_attendance_graph(login_system.users[0])
