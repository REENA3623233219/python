'''Afile contains a word "Donkey" muktiple times. you need to write 
a program which replaces this word with ###### by updating the same file.'''



with open("donkey.txt") as f:
    content = f.read()


content = content.replace("donkey" , "$%^@$^#")

with open("donkey.txt" , "w") as f:
    f.write(content)
