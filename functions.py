# Q1:- Create a function to calculate the area of a circle by taking radius from user.
'''
def circle():
    Pi=3.14
    radius=float(input("Enter the radius of circle:-\t"))
    area = Pi * radius * radius
    print("The area of circle is:-\t",area)
'''

# Q2:- Write a function “perfect()” that determines if parameter number is a perfect number.
#      Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
'''
def perfect(n):
  sum=0
  for i in range(1,n):
    if n%i==0:
      sum=sum+i
  if sum==n:
      return True
  else:
      return False
    
for i in range(1,1000):
  if perfect(i):
    print(i)
'''

# Q3:- Print multiplication table of 12 using recursion.
'''
def multiply(n,m=1):
    print(n*m)
    if m!=10:
        multiply(n,m+1)
'''

# Q4:-  Write a function to calculate power of a number raised to other ( a^b ) using recursion.
'''
def recursion(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*recursion(base,exp-1))
    base=int(input("Enter base: "))
    exp=int(input("Enter exponential value: "))
    print("Final Result:",recursion(base,exp))
'''

# Q5:- Write a function to find factorial of a number but also store the factorials calculated in a dictionary.
n=int(input("Enter the number: "))

def factorial(n):
    if n==1:
      return n
    else:
      return n*factorial(n-1)
f=factorial(n)
print(f)

d={n,f}
print(d)
      
        
