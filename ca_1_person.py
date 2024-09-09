# Greeting function
def greet():
    print("Hello to you")
    print("My Name is JARVIS")
    print("May I know your name?")
    userName = input()
    print(f"Nice to meet you, {userName}!")

greet()


# Class definition
class Student:
    # Constructor to initialize attributes
    def __init__(self, name, age, schoolclass, house, classteacher):
        self.name = name
        self.age = age
        self.schoolclass = schoolclass
        self.house = house
        self.classteacher = classteacher
        print(f"Creating a new student record for {self.name}")

    # Method to change details of the student
    def change_details(self):
        print("Please enter the new age:")
        self.age = int(input())
        print("Please enter the new name of the student:")
        self.name = input()

    # Method to display student details
    def show_details(self):
        print("The details of the student are:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Class: {self.schoolclass}")
        print(f"House: {self.house}")
        print(f"Class Teacher: {self.classteacher}")

# Create two student objects with initial data
varnika = Student(name="Varnika", age=12, schoolclass="6th A", house="Sapphire", classteacher="Poonam Ma'am")
surabhi = Student(name="Surabhi", age=13, schoolclass="7th B", house="Emerald", classteacher="Rajesh Sir")

# Show details of both students
varnika.show_details()
surabhi.show_details()

# Modify details for one of the students
varnika.change_details()
varnika.show_details()
