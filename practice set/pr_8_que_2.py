# Write a python program using function to convert celsius to fahrenheit .



def farh(cel):
    return (cel * (9/5)) + 32


c = int(input("Enter number which you want to change in Fahreheit "))
f = farh(c)
print("Fahreheit Temperature is " + str(f))