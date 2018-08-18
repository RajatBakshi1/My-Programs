# Q1:- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
'''
class Circle:
    def area(radius):
        Pi=3.14
        radius=int(input("Enter the radius of circle:-\t"))
        area=Pi*radius*radius
        print("Area of circle is:-\t",area)

    def circum(radius):
        Pi=3.14
        radius=int(input("Enter the radius of circle:-\t"))
        circumference=2*Pi*radius
        print("Circumference of circle is:-\t",circumference)
'''

# Q2:- Create a Student class and initialize it with name and roll number. Make methods to :
#  1:- Display - It should display all informations of the student.
'''
class Student:
   def info(self,name,roll):
        self.name=name
        self.roll=roll
   def display(self):
        print("My name is ",self.name)
        print("My name is ",self.roll)
'''

# Q3:- Create a Temprature class. Make two methods :
#  1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#  2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
'''
class Temperature:
   def __init__ (self):
      self.cel=int(input("Enter the temperature celsius value to convert it into fahrenheit:-"))
      self.far=int(input("Enter the temperature fahrenheit value to convert it into celsius:-"))
   def temp(self):
      print("celsius value to fahrenheit:",self.cel*9/5+32)
      print("fahrenheit value to celsius:",self.far*32*5/9)
'''

# Q4:-  Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#       Make methods to 
#  1. Display-Display the details.
#  2. Update- Update the movie details.
'''
class MDetails():
   def __init__ (self):
      self.mname=input("Enter the movie name:-\t")
      self.aname=input("Enter the artist name:-\t")
      self.year=int(input("Enter the year of release:-\t"))
      self.rating=float(input("Enter the movie ratings:-\t"))
   def display(self):
      print("Movie name is",self.mname)
      print("Artist name is",self.aname)
      print("Year release of movie is",self.year)
      print("Rating of movie is",self.rating)
   def update(self):
      self.mname=input("Enter the movie name:-\t")
      self.aname=input("Enter the artist name:-\t")
      self.year=int(input("Enter the year of release:-\t"))
      self.rating=float(input("Enter the movie ratings:-\t"))
      print("Movie name is",self.mname)
      print("Artist name is",self.aname)
      print("Year release of movie is",self.year)
      print("Rating of movie is",self.rating)
'''

# Q5:- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
#  1. Display expenditure and savings 
#  2. Calculate total salary
#  3. Display salary
'''
class Expenditure():
   def __init__ (self):
      self.exp=float(input("Enter the expenditure:-"))
      self.saving=float(input("Enter the savings:-"))
   def expenditure(self):
      print("Your expenditure is:-\t",self.exp)
      print("Your savings is:-\t",self.saving)
   def totalsal(self):
      self.tsal=self.exp+self.saving
   def displaysal(self):
      print("Your total salary is:-",self.tsal)
'''   
      
