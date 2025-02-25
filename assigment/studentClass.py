#Write a program to create student class with the following members:
#Data members:
#name, roll, marks
#Member functions:
#__init__(), initialize the object with name, roll
#showdata() display all the details of the student
#showmarks() display marks of the student




class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def showmark(self):
            print(self.marks)

    def showdata(self):
        print(self.name)
        print(self.roll_no)
        
name=input("enter the name: ")
roll_no=int(input("enter ur roll number: "))
marks=list(map(int, (input("enter the marks: ").split())))


ob=Student (name,roll_no,marks)
ob.showdata()
ob.showmark()