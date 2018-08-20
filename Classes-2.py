# Q1:- Create a class Animal as a base class and define method animal_attribute.
#      Create another class Tiger which is inheriting Animal and access the base class method.
'''
class Animal():
    def __init__ (self,place,kind):
        self.place=place
        self.kind=kind
class Tiger(Animal):
    def display(self,food,gender):
        self.food=food
        self.gender=gender
        print("The tiger lives in",self.place)
        print("The tiger is a",self.kind)
        print("The tiger eats",self.food)
        print("The tiger is",self.gender)
'''

# Q2:- What will be the output of following code.
'''
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())
'''

'''
# Output of program is:-

A B
A B
'''

# Q3:- Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details.
#      Create another class Mission which extends the class Cop. Define method add_mission _details.
#      Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.
'''
class Cop():
    name=""
    age=''
    exp=''
    desg=""
    def add(self):
        self.name=input("Enter your name:-\t")
        self.age=int(input("Enter your age:-\t"))
        self.exp=int(input("Enter your work experience in years:-\t"))
        self.desg=input("Enter your designation:-\t")
    def display(self):
        print("My name is ",self.name)
        print("My age is ",self.age)
        print("My work experience is",self.exp)
        print("My designation is",self.desg)
    def update(self):
        self.name=input("Enter your name:-\t")
        self.age=int(input("Enter your age:-\t"))
        self.exp=int(input("Enter your work experience in years:-\t"))
        self.desg=input("Enter your designation:-\t")
        print("My name is ",self.name)
        print("My age is ",self.age)
        print("My work experience is",self.exp)
        print("My designation is",self.desg)
class Mission(Cop):
  def add_mission_details(self,m1):
      print("Mission: ",m1)
      m1 = Mission()
      m1.add()
      m1.display()
      m1.add_mission_details("Kidnapping case of 5 year old boy")
'''

# Q4:- Create a class Shape.Initialize it with length and breadth.Create the method Area. Create class rectangle and square which inherits shape
#      and access the method Area.
'''
class Shape():
    length=int()
    breadth=int()
    def area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        return self.length*self.breadth
class Rectangle(Shape):
    def d_area(self):
        length=int(input("Enter the length:-\t"))
        breadth=int(input("Enter the breadth:-\t"))
        print("Area of Rectangle is  ",self.area(length,breadth))
class Square(Shape):
    def d_area(self):
        a=int(input("Enter the side of square "))
        print("Area of square is ",self.area(a,a))
'''
