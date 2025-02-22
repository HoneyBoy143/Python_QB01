# Write a Python program to implement hierarchical inheritance with at least one base class and two derived classes.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage
dog = Dog()
cat = Cat()
print(dog.speak()) 
print(cat.speak()) 