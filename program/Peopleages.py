# Q5:- Take the input age of 3 people and determine oldest and youngest among them.
first=int(input("Enter first age:"))
second=int(input("Enter second age:"))
third=int(input("Enter third age:"))
if first>second and first>third:
    print("First is oldest...")
if second>first and second>third:
    print("Second is oldest...")
if third>first and third>second:
    print("Third is oldest")
if first<second and first<third:
    print("First is youngest...")
if second<first and second<third:
    print("Second is youngest...")
if third<first and third<second:
    print("Third is youngest...")
if first==second and first==third and second==third:
    print("All are equal in age......")

