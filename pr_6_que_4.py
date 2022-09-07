# Write a program which finds out whether a given username contains less than 10 characters or not .



num = input("Enter user name ")
a = len(num)

if(a<10):
    print("Given user name contains less than 10 characters.")

else:
    print("Given user name donot contains less than 10 characters.")