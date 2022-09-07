# Write a program to create a dictionary of hindi words with values 
# as their english translation provide  user with an option to look it up !



myDict = {
    "Pankha" : "Fan" ,
    "Dabba": "Box" ,
    "Vastu" : "item"
    
}
print("Option are " , myDict.keys())
a = input("Enter the hindi word \n")
# print("The meaning of your word is : " , myDict[a])


# Below line will not throw an error if the key is not present in the dictionary .

print("The meaning of your word is : " , myDict.get(a))