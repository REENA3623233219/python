# Write a python program to rename a file to "renamed_by_python.txt" .



import os


oldname = "pr_9_que_11.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname , "w") as f:
    f.write(content)


os.remove(oldname)