import time
def sum(num1,num2):
    return "the result is:" ,num1 + num2                      
def subtract(num1,num2):
    return "the result is:" , num1 - num2
def multiplication(num1,num2):
    return "the result is:" , num1 * num2
def division(num1,num2):
    try:
        return "the result is:" , num1 / num2
    except ZeroDivisionError:
        print("You cannot divide by 0")
def menu():
    print ('----------------')
    print ('CALCULATOR')
    print ('----------------')

    print('''    1.- Sum 
2.- Subtract
3.- Multiplication
4.- Division''')  

while True: 
    question = input("Do you want to close the program? Yes or No:")
    if question == "no": 
         
        while True:
                try:
                    time.sleep(1)                                
                    menu()
                    person = int ( input ('Choose an operation:'))
                    break
                except ValueError:
                    print ("Choose a number, not a letter")
        while True:
                try:
                    if person == 1:
                        op1 = float(input("Enter the first number: "))
                        op2 = float(input("Enter the second number: "))
                        print(sum(op1,op2))
                        break                                                      
                    else:
                        if person == 2:
                            op1 = float(input("Enter the first number: "))
                            op2 = float(input("Enter the second number: "))
                            print(subtract(op1,op2))
                            break
                        else:
                            if person == 3:
                                op1 = float(input("Enter the first number: "))
                                op2 = float(input("Enter the second number: "))
                                print(multiplication(op1,op2))
                                break
                            else:
                                if person == 4:
                                    op1 = float(input("Enter the first number: "))
                                    op2 = float(input("Enter the second number: "))
                                    print (division(op1,op2))
                                    break
                except ValueError:
                    print ("Enter a number not a letter!!!")
    else:
        if question != "no":
            print ("Good bye")
            time.sleep(1)

            break