numero = int ( input("Cuantos nombres contiene tu lista?:"))

if numero < 1:
    print ("No puede ser!!")
else:
    lista = []
    for i in range(numero):
        print ("Inroduce el " , str (i+1) + ":" ,end="")
        nombre = input()
        lista += [nombre]
    print ("La lista esta conformada por : ", lista)

    buscar = input ("Que nombre desea buscar? :")
    contador = 0

    for i in lista:
        if i == buscar:
            contador += 1; 
    if contador == 0:
        print ("El nombre de " + buscar + " no aparece en esta lista")
    elif contador == 1:
        print ("El nombre de " + buscar + " aparece una vez")
    else:
        print ("El nombre de " + buscar + " aparece " ,contador," veces en la lista")

