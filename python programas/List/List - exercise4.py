numero = int (input("¿Cuantos nombres tendra la lista?"))
if numero < 1:
    print ("No puede ser..")
else:
    lista = []
    for i in range (numero):
        print ("Introduce el",str(i+1),":",end = "")
        nombre = input()
        lista += [nombre]
    print ("Estos nombres esta en la lista: ",lista)
    
    
    eliminar = input ("Introduce un nombre a eliminar: ")
    for i in lista:
        if i == eliminar:
            lista.remove(eliminar)
            print ("Esta es la nueva lista: " , lista)
        elif i != eliminar:
            print ("No se puede elimnar un nombre que no esta en la lista")