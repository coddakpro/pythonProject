class Person:
   def __init__(self, first_name, age):
       self.age = age
       self.first_name = first_name

   def get_age(self):
       return self.age

   def set_age(self, x):
       self.age = x

   def get_first_name(self):
     return self.first_name

   def __set__first_name(self, first_name):
     self.first_name = first_name




