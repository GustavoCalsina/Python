import time
number = int (input("What number am I thinking of? :"))

intento = 0
mynumer =5

while number!=5:
    print ("That's not my number")

    if intento == 2:
        print ("You have reached the maximum number of attempts")
        time.sleep(1)
        print("The program will be closed, goodbye")
        time.sleep(3)
        break
    number = int (input("What number am I thinking of? :"))
    if number!=5:
        intento += 1

if intento<2:
 print ("good")






    


