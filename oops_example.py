# Example of OOP in Python

class Student:
    # Constructor (called when creating a new object)
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    # Method to display student info
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")

    # Method to check eligibility
    def is_eligible(self):
        return self.age >= 18


# Inheritance Example
class GraduateStudent(Student):
    def __init__(self, name, age, roll_no, degree):
        super().__init__(name, age, roll_no)  # Call parent constructor
        self.degree = degree

    def display_info(self):
        super().display_info()
        print(f"Degree: {self.degree}")


# ---- Usage ----
# Create Student object
s1 = Student("Rohit", 17, 101)
s1.display_info()
print("Eligible:", s1.is_eligible())

print("-----")

# Create GraduateStudent object
s2 = GraduateStudent("Anita", 22, 102, "M.Sc. Computer Science")
s2.display_info()
print("Eligible:", s2.is_eligible())
