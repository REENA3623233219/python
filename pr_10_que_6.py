'''Can you change the self parameter inside a class to samething else (say 'harry').
 Try changing self to 'SLF' or 'harry' and see the effects.'''



class Sample: 
    def __init__(slf, name):
        slf.name = name

obj = Sample("Harry") 
print(obj.name) 