# Q1:-  Name and handle the exception occured in the following program:
'''
a=3
if a<4:
    try:
        a=a/(a-3)
        print(a)
    except ZeroDivisionError:
        print("The Zero Division Error has occurred here")

# In this Zero Division Error was occurring.
'''

# Q2:- Name and handle the exception occurred in the following program:
'''
def list():
    try:
        l=[1,2,3]
        print(l[3])
    except IndexError:
        print("Index error has occurred")


# In this Index Error has occurred.
'''

# Q3:- What will be the output of the following code:
'''
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise

# Output:- NameError : Hi there
'''

# Q4:- What will be the output of the following code:
'''
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

# OUTPUT OF PROGRAM IS :- -5.0
#                      :-   a/b result in 0
'''

# Q5:- Write a program to show and handle following exceptions: 
#  1. Import Error
#  2. Value Error
#  3. Index Error

# 1:- Import error
'''
def me():
    try:
        time.time()
        print("time")
    except:
        print("Import error")
'''
# 2:- Value Error
'''
def val():
    try:
        for i in range(5):
            i=int(input("Enter value "))
            print("Your Value of entered number is",i)
    except:
        print("Value error has occurred")
'''
# 3:- Index Error
'''
def new():
    try:
        L=[1,2,3,4,5]
        print(L[6])
    except IndexError:
        print("Index error has occurred")
'''
        
# Q6 :-  Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
#        The code must keep taking input till the user enters the appropriate age number(less than 18).
'''
def code():
    try:
        age=int(input("Enter your age"))
        if age<=18:
            raise ValueError("AgeTooSmallError")
    except ValueError:
        print("Age too small Error()")
    else:
        print("You are eligible")
'''

