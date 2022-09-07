# Write a program to fill in a letter template given below with name and date .

#             letter = '''Dear <|NAME|>
#                              You are selected!
#                             <|DATE|>'''



letter = '''Dear <|Name|>,
            You are selected !
            Date: <|Date|>
'''
Name = input("Enter your Name :-")
Date = input("Enter Date :-")
letter = letter.replace("<|Name|>" ,Name)
letter = letter.replace("<|Date|>" ,Date)
print(letter)