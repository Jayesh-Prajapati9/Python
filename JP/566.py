class Student():
    studentName=""
    studentMarks1=0
    studentMarks2=0
    studentRoll=0
    l=list()
    def __init__(self,name,marks1,marks2,rollno):
        self.studentName=name
        self.studentRoll=rollno
        self.studentMarks1=marks1
        self.studentMarks2=marks2
        Student.l.append(self)
    def accpet(self):
        name=input("Enter Your name : ")
        rollno=int(input("Enter Your Roll No : "))
        marks1=int(input("Enter Your Marks Of Subject 1: "))
        marks2=int(input("Enter Your Marks Of Subject 2: "))
        student=Student(name,marks1,marks2,rollno)
    def display(self):
        for i in self.l:
            print("Student ${i} Name :",i.studentName)
            print("Student ${i} Roll No :",i.studentRoll)
            print("Student ${i} Marks Of Sub 1 :",i.studentMarks1)
            print("Student ${i} Marks Of Sub 2 :",i.studentMarks2)
    def delete(self):
        rollno=int(input("Enter The Roll No : "))
        for i in self.l:
            if(i.studentRoll==rollno):
                self.l.remove(i)
                break
        else:
            print("Student Not Found")
    def search(self):
        rollno=int(input("Enter The Roll No : "))
        for i in self.l:
            if(i.studentRoll==rollno):
                print(f"\nStudent {i} Name :",i.studentName)
                print(f"Student {i} Roll No :",i.studentRoll)
                print(f"Student {i} Marks Of Sub 1 :",i.studentMarks1)
                print(f"Student {i} Marks Of Sub 2 :",i.studentMarks2)
                break
        else:
            print("Student Not Found")
    def update(self):
        oldrollno=int(input("Enter The Roll No : "))
        for i in self.l:
            if(i.studentRoll==oldrollno):
                newrollno=int(input("Enter The New Roll No : "))
                i.studentRoll=newrollno
                break
        else:
            print("Student Not Found")
        
s=Student("A",85,90,1)

s.accpet()
s.accpet()
s.accpet()
s.display()
s.search()
s.delete()
s.update()