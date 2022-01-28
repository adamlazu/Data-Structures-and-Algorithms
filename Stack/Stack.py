#This is the implementation of stack in python language
def createStack():
    stack = []
    return stack
    #this function will return a list that will be used as a stack

def push(stack, item):
    return stack.append(item)
    #this function is designed to add an item into the top of stack

def pop(stack):
    if len(stack) == 0:
        print("stack is already empty")
    else:
        return stack.pop()
    #this function will remove and return the item from the top of the stack

def checkEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False
    #it will return True if the stack is empty



stack = createStack()
push(stack, 2)
push(stack, 5)
push(stack, 1)
print(pop(stack))
print(pop(stack))