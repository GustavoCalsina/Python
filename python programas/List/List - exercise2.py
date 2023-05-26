# Crea una una lista donde tengas que añadir nombre y luego imprimirlos..... 
# 1
"""nombres = []
person1 = int (input  ( "Cuantos nombre tien tu lista ? : "))

if person1 == 0 :
    print ("No  puede ser ....")

else:
    if person1 == 3:
    
        lista = input ("Introduce el primer nombre :")
        nombres.append(lista)
        lista = input ("Introduce el primer nombre :")
        nombres.append(lista)
        lista = input ("Introduce el primer nombre :")
        nombres.append(lista)
        
        print (nombres)"""
            

#resultado 

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)



