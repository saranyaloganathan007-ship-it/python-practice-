class Student:
    def __init__(self):
        self.__name = "Saranya"

    def get_name(self):
        return self.__name


student = Student()

print("Student Name:", student.get_name())