#this program will convert a decimal number into another numerical systems

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


decimal = int(input("input number in decimal: "))
binary = createStack()
octal = createStack()
hexadecimal = createStack()

n = decimal
while n!= 0:
    rem = n%2
    push(binary, rem)
    n=n//2

n = decimal
while n!= 0:
    rem = n%8
    push(octal, rem)
    n=n//8

hexa = {10:'A', 11:'B', 12:'C', 13:'D',
        14:'E', 15:'F'}

n = decimal
while n!= 0:
    rem = n%16
    if rem<=9:
        push(hexadecimal, rem)
    else:
        push(hexadecimal, hexa[rem])
    n=n//16

print("your number in binary is:")
while len(binary)!=0:
    print(pop(binary),end="")
print("")
print("your number in octal is:")
while len(octal)!=0:
    print(pop(octal),end="")
print("")
print("your number in hexadecimal is:")
while len(hexadecimal)!=0:
    print(pop(hexadecimal),end="")
