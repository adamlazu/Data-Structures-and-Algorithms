#This program is one of the application from the stack data structures
#This program will reverse a string

def createStack():
    stack =[]
    return stack

def push(stack, item):
    return stack.append(item)

def pop(stack):
    if len(stack) == 0:
        print("stack is already empty")
    else:
        return stack.pop()

def checkEmpty(stack):
    if len(stack)==0:
        return True
    else:
        return False

stack = createStack()
string = input("input string that will be reversed: ")

for i in range (len(string)):
    push(stack,string[i])

print("the reversed string is:")

for i in range(len(stack)):
    print(pop(stack), end="")
