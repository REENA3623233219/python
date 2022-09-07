# Repeat program 4 for a list of such words to be censored.




words = ["donkey" , "kaddu" , "mote"]


with open("pr_9_que_5.txt") as f:
    content = f.read()


for word in words:
    content = content.replace(word , "$%^@$^#")

with open("pr_9_que_5.txt" , "w") as f:
    f.write(content)
