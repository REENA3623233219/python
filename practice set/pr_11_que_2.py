# Creat a class pets from a class animals and fuether creat class dog from pets. add a method bark to class Dog.




class Animals:
    animalType = "Mammal"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow bow!")

d  = Dog()
d.bark()