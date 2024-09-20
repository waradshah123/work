def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y 

def divide(x,y):
    if y ==0:
        return "Maths Error!No number can be divided by zero it will give us infinity"
    else:
        return x/y

def modulus(x,y):
    return x % y
def exponentiate(x,y):
    return x**y
def menu():
    print("select ur operation")
    print("1-- ADD")
    print("2--SUBTRACT")
    print("3--MULTIPLY")
    print("4--DIVIDE")
    print("5--MODULUS")
    print("6--EXPONENTIATION")
def calculator():
    while True:
        menu()
        choice =input("enter ur choice(1/2/3/4/5/6 or 'q' to Quit):")
        if choice == "q":



            print("u have exited the calculator")
            break
        if choice in ['1','2','3','4','5','6']:
            try:
                num1 =float(input("enter ur first number :"))
                num2 =float(input("enter ur second number:"))
            except ValueError:
                print("invalid input!!!!!!!! please enter only numeric values")
                continue
            
            if choice=='1':
                PRINT(F"{num1}+{num2}={add(num1,num2)}")

            elif choice =='2':
                 print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            elif choice == '5':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")

            elif choice == '6':
                print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")

        else:
            print("Invalid Input! Please select a valid operation.")


calculator()

         





    
