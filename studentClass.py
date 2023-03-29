#!/usr/bin/env python

class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)

# Write a main()
def main():
    # Create 2 student objects and print them
    student1 = Student("Silang", "Diego", "Science", 1.5)
    student2 = Student("Bonifacio", "Andress", "Math", 1.2)
    print("Student1 :",student1)
    print("Student2 :",student2)
    
# let's do the test :)
if __name__ == '__main__':
    main()
