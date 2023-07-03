from model.newstudent import Student
from config import Client

def add_student(name, password, course ,schoolname ,emailid , mobileno, sex, address):
    student = Student(name, password,course ,schoolname ,emailid , mobileno, sex, address)
    db = Client["studentdata"]
    registered_students = db["registeredstudents"]
    get_studentdata= student.get_student_data()
    if get_studentdata == None:
        print('get_studentdata',get_studentdata)
        student.save()
        return True
    else:
        print('already exists')
        return False