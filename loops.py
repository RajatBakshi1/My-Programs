# Q1:- Take 10 integers from user and print it on screen.
'''
integer=1
while integer<=10:
    print("Value of integer is:",integer)
    integer += 1
'''

# Q2:- Write an infinite loop.An infinite loop never ends. Condition is always true.
'''
while True:
    print("\t The program will run INFINITE times as the condition is always true")
'''

# Q3:- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
'''
a=[1,2,3,4,5]
b=[]
for i in a:
    b.append(i*i)
    print(b)
'''

# Q4:- From a list containing ints, strings and floats, make three lists to store them separately.
'''
l=['a','b','c',10,20,30,1.4,53.76,78.53]
m=[]
n=[]
o=[]
for x in range(0,len(l)):
    if type(l[x])==float:
        m.append(l[x])
    elif type(l[x])==int:
        n.append(l[x])
    else:
        o.append(l[x])
print(m,n,o)
'''

# Q5:-Using range(1,101), make a list containing even and odd numbers.
'''
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even number list:\n",even)
print("Odd number list:\n",odd)
'''

# Q6:- Q.6- Print the following patterns: 
#      *
#      **
#      ***
#      ****
'''
for x in range(5):
    print("*"*x)
'''

# Q7:- Create a user defined dictionary and get keys corresponding to the value using for loop.
'''
names=['Rajat','Ashish','Param','Naveen','Sahil','Vedant','Puru','Nitin','Manas']
marks=[84,77,95,65,75,57,98,50,87]
dict={}
for i in range(len(names)):
    dict[names[i]]=marks[i]
for i in dict.keys():
    print(i)
'''

# Q8:- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element,
#      if found. Iterate over list using for loop.
'''
print("Enter the values for the list:")
hello=[]
hello=[str(x) for x in input().split()]
value=input("Value to be deleted from the list:")
for x in hello:

    if x==value:
        hello.remove(x)
'''
print(hello)
    

    


    
    
