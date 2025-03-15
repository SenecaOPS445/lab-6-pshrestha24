#!/usr/bin/env python3
# Author ID: 158131227

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensure number is stored as a string
        self.courses = {}
    
    def displayStudent(self):
        return f'Student Name: {self.name}\nStudent Number: {self.number}'
    
    def addGrade(self, course, grade):
        self.courses[course] = grade
    
    def displayGPA(self):
        if not self.courses:
            return f'GPA of student {self.name} is 0.0'  # Prevent division by zero
        total_gpa = sum(self.courses.values())
        avg_gpa = total_gpa / len(self.courses)
        return f'GPA of student {self.name} is {avg_gpa:.1f}'
    
    def displayCourses(self):
        return [course for course, grade in self.courses.items() if grade > 0.0]

if __name__ == '__main__':
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    student2 = Student('Jessica', 123456)  # Integer number should work fine
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
