# Write a program to calsulate the factorial of a given numbers using for loop.



num = int(input("Enter the number : "))
factorial = 1

for i in range(1, num+1):
    factorial = factorial * i

print(f"The factorial of this {num} is {factorial}")