# Write a program to find out the line numbers where python is present from que 6 .




content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content .lower():
            print(content)
            print(f"Yes python is present {i}")
            print(i)
        i+=1
