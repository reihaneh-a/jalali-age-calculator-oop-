import jdatetime
class Person:
  def __init__(self, name, birthday):
     self.name = name
     self.birthday = birthday


  def display(self):
      return f'name is:{self.name} \t age is:{jdatetime.datetime.now().year - self.birthday}'

  def __str__(self):
      return f'name is:{self.name} \t age is:{jdatetime.datetime.now().year - self.birthday}'




#===================constructor

p1=Person("ali" , 1382)


print(p1.display())



print(p1)
