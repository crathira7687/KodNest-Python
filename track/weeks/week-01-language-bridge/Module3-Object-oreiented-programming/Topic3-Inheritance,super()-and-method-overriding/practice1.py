class Person:
    def display_name(self, name):
        self.name = name

class Student(Person):
    pass

name = input("enter the name:").strip()
student = Student()
student.display_name(name)
print("Student Name:",student.name)