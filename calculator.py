

    
    
def add(a,b):
    return a+b

def subract (a,b):
    return a-b

def multiplication (a,b):
    return a*b

def divide (a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return("cannot divide by zero")

print("select option")
print("1.Add")
print("2.subract")
print("3.mmultiplication")
print("4.divide")

choice = float(input("Enter the option:-"))

if choice in [1,2,3,4]:
    try:
        number1 =float (input("Enter the first number:-"))
        number2 = float (input("Enter the second number:-"))

        if choice == 1:
            print(f"Result is {add(number1,number2)}")
        elif choice ==2:
            print(f"Result is {subract(number1,number2)}")
        elif choice == 3:
            print(f"Result is {multiplication(number1,number2)}")
        elif choice == 4:
             print(f"Result is {divide(number1,number2)}")
    except ValueError:
        print("Enter the  number between 1 to 4")


else:
        print("Enter the  number between 1 to 4")
