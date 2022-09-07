# Write a python function to remove a given word from a string and strip it at the same time .



def remove_and_strip(string , word):
    newStr = string.replace(word , "")
    return newStr.strip()

this = "      He is good boy       "
n = remove_and_strip(this, "He")
print(n)

