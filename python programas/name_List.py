import time
number = int(input("Wie viele Namen möchten Sie einfügen? "))

if number < 1:
    print ("es kann nicht sein!!")
else:
    namen_list = []

    for i in range (number):

      print (f"Geben Sie den {str(i+1)} Namen ein :",end="" )
      name = input()
      namen_list +=[name]
    
    print (namen_list)

print ("Möchten Sie einen weiteren Namen hinzufügen ??")

add = input(" Ja oder Nein :")

if add == "Nein":
    print ("Ende des Programms...")
    time.sleep(2)

else:
    if add == "Ja":
        for i in namen_list:
            print("Geben Sie den Namen ein, den Sie hinzufügen möchten:",end="")
            number = int(input())

            for i in range (number):
                print (f"Geben Sie den {str(i+1)} Namen ein :",end="" )
                name = input()
                namen_list +=[name]
            print (namen_list)
            break
    
print ("Möchten Sie einen Namen löschen ??")

remove = input("Ja oder Nein:")
if remove == "Nein":
    print ("Ende des Programms")
else:
    if remove == "Ja":
        number =int(input("Wie vielen Namen möchten Sie löschen?: "))

        for i in range(number):

            print (f"Geben Sie den {str(i+1)} Namen ein :",end="")

            namen_list.remove(input())
        print (f"Das is die neue Liste {namen_list}")
   


  