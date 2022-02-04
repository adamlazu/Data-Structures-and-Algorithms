#this program will convert a decimal number into another numerical systems

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


decimal = int(input("input number in decimal: "))
binary = stack()
octal = stack()
hexadecimal = stack()

n = decimal
while n!= 0:
    rem = n%2
    binary.push(rem)
    n=n//2

n = decimal
while n!= 0:
    rem = n%8
    octal.push(rem)
    n=n//8

hexa = {10:'A', 11:'B', 12:'C', 13:'D',
        14:'E', 15:'F'}

n = decimal
while n!= 0:
    rem = n%16
    if rem<=9:
        hexadecimal.push(rem)
    else:
        hexadecimal.push(hexa[rem])
    n=n//16

print("your number in binary is:")
while len(binary.stack)!=0:
    print(binary.pop(),end="")
print("")
print("your number in octal is:")
while len(octal.stack)!=0:
    print(octal.pop(),end="")
print("")
print("your number in hexadecimal is:")
while len(hexadecimal.stack)!=0:
    print(hexadecimal.pop(),end="")
