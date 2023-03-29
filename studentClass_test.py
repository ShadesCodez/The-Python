#!/usr/bin/env python

import unittest

from studentClass import Student

class TestStudentClass(unittest.TestCase):

    def setUp(self):
        self.lname = "rizal"
        self.fname = "jose"
        self.major = "optalmology"
        self.gpa = 1.0
        self.student = Student(self.lname, self.fname, self.major, self.gpa)
        
    def test_object_created_required_attributes(self):
        actual = Student(self.lname, self.fname, self.major)
        
        self.assertEqual(actual.last_name, self.lname)
        self.assertEqual(actual.first_name, self.fname)
        self.assertEqual(actual.major, self.major)


    def test_object_created_all_attributes(self):
  
        actual = Student(self.lname, self.fname, self.major, self.gpa)


        self.assertEqual(actual.last_name, self.lname)
        self.assertEqual(actual.first_name, self.fname)
        self.assertEqual(actual.major, self.major)
        self.assertEqual(actual.gpa, self.gpa)


    def test_student_str(self):
        actual = str(self.student)
        expected = self.lname + ", " + self.fname + " has major " + self.major + " with gpa: " + str(self.gpa)

        self.assertEqual(actual, expected)
        

    def test_object_not_created_error_last_name(self):
        try:

            actual = Student(fname=self.fname, major=self.major, gpa=self.gpa)
        except TypeError as actual:
            expected = "__init__() missing 1 required positional argument: 'lname'"


            self.assertEqual(str(actual), expected)


    def test_object_not_created_error_first_name(self):
        try:
            actual = Student(lname=self.lname, major=self.major, gpa=self.gpa)
        except TypeError as actual:
            expected = "__init__() missing 1 required positional argument: 'fname'"

            self.assertEqual(str(actual), expected)


    def test_object_not_created_error_major(self):
        try:

            actual = Student(lname=self.lname, fname=self.fname, gpa=self.gpa)
        except TypeError as actual:
            expected = "__init__() missing 1 required positional argument: 'major'"


            self.assertEqual(str(actual), expected)


    def test_object_not_created_error_gpa(self):
        try:
            actual = Student(lname=self.lname, fname=self.fname, major=self.major)

            expected_gpa = 0.0
        
            self.assertEqual(actual.last_name, self.lname)
            self.assertEqual(actual.first_name, self.fname)
            self.assertEqual(actual.major, self.major)
            self.assertEqual(actual.gpa, expected_gpa)
        except TypeError as actual:
            expected = "__init__() missing 1 required positional argument: 'gpa'"

            self.assertEqual(str(actual), expected)

    def test_object_gpa_float(self):
        actual = Student(self.lname, self.fname, self.major, self.gpa)
     
        self.assertEqual(actual.last_name, self.lname)
        self.assertEqual(actual.first_name, self.fname)
        self.assertEqual(actual.major, self.major)
        self.assertEqual(actual.gpa, self.gpa)
        self.assertEqual(type(actual.gpa), type(self.gpa))
        self.assertEqual(isinstance(actual.gpa, float), isinstance(self.gpa, float))
 
def main():
    student1 = Student("Silang", "Diego", "Science", 1.5)
    student2 = Student("Bonifacio", "Andress", "Math", 1.2)
    print("Student1 :",student1)
    print("Student2 :",student2)
    
if __name__ == '__main__':
    main()
    unittest.main()