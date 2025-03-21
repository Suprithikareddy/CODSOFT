print("Welcome to the calculator app.")

def add():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("Addition of the entered numbers is = "+str(num1 + num2))

def sub():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("Subtraction of the entered numbers is = "+str(num1 - num2))

def mul():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("Multiplication of the entered numbers is = "+str(num1 * num2))

def div():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("Division of the entered numbers is = "+str(num1 / num2))

while(True):
    print("Please choose any one of the following options:")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")

    operation = int(input("Enter any choice:"))
    if(operation==1):
        add()
    elif(operation==2):
        sub()
    elif(operation==3):
        mul()
    elif(operation==4):
        div()
    else:
        print("Invalid operation.Please try again.")
    