# Q1:- Create a threading process such that it sleeps for 5 seconds and then prints out a message.
'''
from threading import *
import time
def thread():
    i=1
    while(i<=10):
        time.sleep(5)
        print("My name is Rajat..."+str(i)+"run by"+str(current_thread().getName()))
        i=i+1
def main():
    t1=Thread(target=thread,name=First)
    t1.start()
'''

# Q2:- Make a thread that prints numbers from 1-10, waits for 1 sec between.
'''
from threading import *
import time
def numbers():
    i=1
    while(i<=10):
        time.sleep(1)
        print("Value is:\t"+str(i)+"\t"+str(current_thread().getName()))
        i=i+1
def fun():
    t1=Thread(target=numbers,name=Rajat)
    t1.start
'''

# Q3:- Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#      Delay goes like 2sec-4sec-6sec-8sec-10sec.
'''
from threading import *
import time
a=[1,3,5,7,9]
def element():
    delay=2
    for i in a:
        print("Your valus is:\t",i)
        time.sleep(delay)
        delay+=2
def main():
    t1=Threads(target=element)
    t1.start()
'''

# Q4:- Call factorial function using thread.
'''
from threading import *
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
    f=fact(n)
    print("The factorial of entered number is:-\t",f)
def super():
    t1=Thread(target=fact)
    t1.start()
'''

        
