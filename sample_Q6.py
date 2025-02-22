#Write a Python program to demonstrate method polymorphism

class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

def make_sound(animal):
    print(animal.sound())

cat = Cat()
dog = Dog()

make_sound(cat)
make_sound(dog)