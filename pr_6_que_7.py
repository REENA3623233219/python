# Write a program to find out whether a given post is taking about "Harry" or not .




names = ["Harry"]
name = input("Enter the name to check ")

if name in names:
    print("Given post is talking about Harry.")

else:
    print("Given post is not talking about Harry.")