# Q1:-  Write a Python program to read last n lines of a file.
'''
file=open("C:\\Users\\Genius\\Desktop\\Rajat\\Paragraph.txt")
last=file.readlines()
file.close()
print(last[-1])
'''

# Q2:-  Write a Python program to count the frequency of words in a file.
'''
file=open("C:\\Users\\Genius\\Desktop\\Rajat\\Paragraph.txt")
file.read()
a=file.tell()
print(a)
'''

# Q3:-  Write a Python program to copy the contents of a file to another file.
'''
with open("C:\\Users\\Genius\\Desktop\\Rajat\\Paragraph.txt") as f:
    with open("C:\\Users\\Genius\\Desktop\\Rajat\\New.txt", "w") as f1:
        for line in f:
            f1.write(line)
'''

# Q4:- Write a Python program to combine each line from first file with the corresponding line in second file.
'''
with open("C:\\Users\\Genius\\Desktop\\Rajat\\New.txt") as one,open("C:\\Users\\Genius\\Desktop\\Rajat\\Second.txt") as two:
    for l1,l2 in zip(one,two):
        print(l1+l2)
'''

# Q5:-  Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
'''
import random
with open("C:\\Users\\Genius\\Desktop\\Rajat\\random.txt","w") as a:
    for i in range(10):
        r=str(random.randint(1,10))
        a.writelines(r+'\n')
        print(r)
with open("C:\\Users\\Genius\\Desktop\\Rajat\\random.txt") as a,open("C:\\Users\\Genius\\Desktop\\Rajat\\third.txt","w") as r2:
    b=a.read().splitlines()
    b.sort()
    for i in b:
            r2.write(str(i)+'\n')
'''
