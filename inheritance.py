class Person:
    def show_name(self):
        print("Name: Saranya")


class Student(Person):
    def show_course(self):
        print("Course: Information Technology")


student = Student()
student.show_name()
student.show_course()