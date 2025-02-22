#Write a Python program to implement a stack using push, pop, and display functions

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f'Item {item} pushed to stack.')

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f'Item {item} popped from stack.')
            return item
        else:
            print('Stack is empty.')
            return None

    def display(self):
        if not self.is_empty():
            print('Stack elements are:')
            for item in reversed(self.stack):
                print(item)
        else:
            print('Stack is empty.')

    def is_empty(self):
        return len(self.stack) == 0

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    stack.pop()
    stack.display()