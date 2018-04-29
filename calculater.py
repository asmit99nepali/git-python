__author__ = 'Asmit'
num1 = input("Enter your first number\n")
num2 = input("Enter your Second number\n")
print("Operation\t\t\t\tKeys")
print("*****************************")
print("Add\t\t\t\t\t\tA")
print("Sub\t\t\t\t\t\tS")
print("Multiply\t\t\t\tM")
print("Division\t\t\t\tD")
operation = input("Press your choice\n")
def addition(x=num1,y=num2):
    sum = float(x)+float(y)
    return(print("Sum of your number is ",sum))

def difference(x=num1, y=num2):
    sub = float(x)-float(y)
    return(print("Sum of your number is ",sub))

def multiply(x=num1, y=num2):
    product = float(x)*float(y)
    return(print("Sum of your number is ",product))

def division(x=num1, y=num2):
    part = float(x)/float(y)
    return(print("Sum of your number is ",part))

if(operation=='A'):
    addition(num1,num2)
elif(operation=='S'):
    difference(num1,num2)
elif(operation=='M'):
    multiply(num1,num2)
elif(operation=='D'):
    division(num1,num2)
else:
    print("Sorry your choice is not here")

input("Press Enter to exit")