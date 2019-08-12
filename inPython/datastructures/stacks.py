'''
Stack implementation using lists
'''

class Stack:

    def __init__ (self):
        self.stack = []
    
    def empty_stack (self):
        return self.stack == []
    
    def push (self, data):
        self.stack.append(data)
    
    def pop (self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    def peek (self):
        return self.stack[-1]

    def stack_size (self):
        return len(self.stack)

    def show_stack (self):
        return self.stack

# initializing class and methods
init_stack = Stack()
init_stack.push(4)
init_stack.push(2)
init_stack.push(345)
init_stack.push(22)
print(init_stack.stack_size())
print(init_stack.show_stack())
print(init_stack.peek())