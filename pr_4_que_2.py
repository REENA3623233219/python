# Write a program to accept marks of 6 students and display then in a sorted name .



m1 = int (input("Enter marks of student :-"))
m2 = int (input("Enter marks of student:-"))
m3 = int (input("Enter marks of student:-"))
m4 = int (input("Enter marks of student:-"))
m5 = int (input("Enter marks of student :-"))
m6 = int (input("Enter marks of student :-"))

mylist = [m1 , m2 , m3 ,m4 , m5 , m6]
mylist.sort()
print(mylist)
