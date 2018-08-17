# Q1:- What is Time Tuple?
'''
import time
print(time.time())

print(time.asctime())

print(time.gmtime())

print(time.perf_counter())

print(time.localtime())

print(time.ctime())

print(time.timezone)

'''

# Q2:- Write a program to get formatted time.
'''
import time
import os
while True:
    print(time.strftime("%H:%M:%S"))
    time.sleep(1)
    os.system('cls')
'''

# Q3:- Extract month from the time.
'''
import datetime
a="16-8-2018"
d=datetime.datetime.strptime(a,"%d-%m-%Y")
print(d.month)
'''

# Q4:- Extract day from the time.
'''
import datetime
a="16-8-2018"
d=datetime.datetime.strptime(a,"%d-%m-%Y")
print(d.day)
'''

# Q5:- Extract date (ex : 11 in 11/01/2021) from the time.
'''
import datetime
d=datetime.date.today()
print(d)
'''

# Q6:- Write a program to print time using localtime method.
'''
import time
t=time.localtime()
print(t)
'''

# Q7:- Find the factorial of a number input by user using math package functions.
'''
n=int(input("Enter any number to find it's factorial:- "))
import math
f=math.factorial(n)
print(f)
'''

# Q8:- Find the GCD of a number input by user using math package functions.
'''
import math
x=int(input("Enter first number:- "))
y=int(input("Enter second number:- "))
new=math.gcd(x,y)
print(new)
'''
