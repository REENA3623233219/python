'''Create a class with a class attribute a ; create an object from 
it and set a direclty using object a = 0. does this change this class attribute .'''



class Sample:
    a = "Harry"

obj = Sample()
obj.a = "Vikky"
# Sample.a = "Vikky"

print(Sample.a)
print(obj.a)