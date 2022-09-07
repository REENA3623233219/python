# Write a recursive function to calculate the sum of frist n natural numbers .



def sumN(n):
    if n==1:
        return 1

    else:
        return sumN(n-1) + n

num = int(input("Enter any number  "))
if num<0:
    print("Enter a positive number  ")

else:
    print("The sum is " , sumN(num))