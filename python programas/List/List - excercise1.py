numero = int (input("Introduce el numero de nombres que deseas añadir en la lista: "))

if numero <1:
    print ("No puede ser..")
else:
    lista = []
    for i in range (numero):
        print ("Introduce el",str(i+1),"nombre :",end="")
        nombre = input()
        lista += [nombre]
    print ("En la lista estan añadidos :",lista)

eliminar = int(input("Introduce el numero de nombres que deseas de eliminar en la lista :"))

if eliminar < 1 :
    print ("Fin del programa")

else:
    
    for i in range (eliminar):

        print (f"Introduce el {str(i+1)} nombre :",end="")
        
        lista.remove(input())
    print(f"La nueva lista es {lista}")
        
       
    

      
