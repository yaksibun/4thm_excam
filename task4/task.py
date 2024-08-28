class Person:
  def __init__(self, name: str, age: int):
    self.Name = name
    self.age = age
    
  def get_info(self):
    return print(f"""
Name: {self.Name}
age: {self.age}""")  
  def works(self):
    return print("I work")
  
class Teacher(Person):
  def __init__(self, name: str, age: int, subject: str):
    
    self.subject = subject
    super().__init__(name, age)
    
  def works(self):
    # return super().works("I teach")
    return print(f"I teach: {self.subject}")
  
class Student(Person):
  def __init__(self, name: str, age: int, grade:int):
    self.grade = grade
    super().__init__(name, age)   
    
  def works(self): 
    # return super().works("I study")  
    return print(f"I study: {self.grade}")

print("Teacher")
teacher = Teacher(input("Enter your name: "), int(input("Enter your age: ")), input("Enter your subject: "))
print("Student")
student = Student(input("Enter your name: "), int(input("Enter your age: ")), int(input("Enter your grade: ")))

teacher.get_info()
teacher.works()

student.get_info()
student.works()
