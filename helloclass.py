def calculate_iq(studentage, student_brain_size, student_years_game):
   return studentage + student_brain_size + student_years_game


student1_age=12
student1_brain_size =1
student1_years_game=10
print(calculate_iq(student1_age, student1_brain_size, student1_years_game))

student1_age=13
student2_brain_size =10
student2_years_game=122
print(calculate_iq(student1_age, student2_brain_size, student2_years_game))

class Student:
   def __init__(self, age, brain_size, years_game):
      self.age = age
      self.brain_size = brain_size
      self.years_game = years_game

   def calculate_iq(self):
      return self.age + self.brain_size + self.years_game

s1 = Student(1,10,100)
print(s1.calculate_iq())

s1 = Student(age=2,brain_size=10,years_game=100)
print(s1.calculate_iq())

