# Write a Python program to implement multiple inheritance with at least two parent classes and one child class.

class Parent1:
    def __init__(self):
        self.str1 = "Parent1"
    
    def display_str1(self):
        print(self.str1)

class Parent2:
    def __init__(self):
        self.str2 = "Parent2"
    
    def display_str2(self):
        print(self.str2)

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
    
    def display_all(self):
        self.display_str1()
        self.display_str2()

c1 = Child()
c1.display_all()