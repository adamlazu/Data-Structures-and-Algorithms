#This program is one of the application from the stack data structures
#This program will reverse a string

class stack:
    def __init__(self):
        self.stack=[]

    def push(self, item):
        return self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[len(self.stack)-1]
    
    def checkEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False

stack = stack()
string = input("input string that will be reversed: ")

for i in range (len(string)):
    stack.push(string[i])

print("the reversed string is:")

for i in range(len(stack.stack)):
    print(stack.pop(), end="")
