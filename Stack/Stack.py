#This is the implementation of stack in python language

class stack:
    def __init__(self):
        self.stack=[]
        #this is the constructor to create a stack

    def push(self, item):
        return self.stack.append(item)
        #a method for push an item into the stack
    
    def pop(self):
        return self.stack.pop()
        #this method will pop or remove the item on top of the stack
    
    def peek(self):
        return self.stack[len(self.stack)-1]
        #will return an item that is on the top of the stack
        #without removing it
    
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
        #will check whether the stack itself is empty or not


stack = stack()
stack.push(1)
stack.push(5)
stack.push(7)

print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.peek())

