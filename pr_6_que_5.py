# Write a program which finds out whether a given name is present in a list or not .



names = ["Ram" , "Sita" , "Gita" , "Rama" , "Shyam" , "Mohan"]
name = input("Enter the name to check ")

if name in names:
    print("Your name is present in the list")

else:
    print("Your name is not present in the list")