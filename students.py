class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Grade: {self.grade}")
        print("-" * 30)


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been added to {self.school_name}.")

    def show_all_students(self):
        print(f"\nStudents of {self.school_name}:")
        for student in self.students:
            student.display_info()

# Example usage
if _name_ == "_main_":
    # Create a school
    my_school = School("Green Valley High School")

    # Create students
    s1 = Student("Alice", 101, "A")
    s2 = Student("Bob", 102, "B+")
    s3 = Student("Charlie", 103, "A-")

    # Add students to the school
    my_school.add_student(s1)
    my_school.add_student(s2)
    my_school.add_student(s3)

    # Display all students
    my_school.show_all_students()
