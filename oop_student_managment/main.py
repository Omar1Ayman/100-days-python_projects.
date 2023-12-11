class School:
    def __init__(self):
        self.students = []
    def add_student(self,name,age,roll_number):
        student = Student(name,age,roll_number)
        self.students.append(student)
        
    def get_students(self):
        for stu in self.students:
            print(f"name: {stu.name}")
            print(f"age: {stu.age}")
            print(f"roll number: {stu.roll_number}")
            print("="*20)
        


class Student:
    def __init__(self,name,age,roll_number):
        self.name = name
        self.age =age
        self.roll_number = roll_number

school = School()
repeat = True
while repeat:
    choose = input("chosse number\n1) 1-add new student\n2) 2-show students\n 3-edit student\n 4-delete student\n 5-quite: ")
    if choose == "1":
        name = input("name: ")
        age = int(input("Age: "))
        roll_number = int(input("roll number: "))
        school.add_student(name,age,roll_number)
    if choose == "2":
        school.get_students()
    
    
    
    
