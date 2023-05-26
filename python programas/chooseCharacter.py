import time
def race_3():
    print ("You chose the Monster race....")
    time.sleep(0.5)

    race_3 = {
        "life :" : 8000,
        "Damage :" : 150,
        "Critical Damage" : 170
    }

    for x,y in race_3.items():

        print (x,y)
      
        
    print ("If you wish to change race, press the f key.")
    print ("If you wish to continue press g")

    person1 = input ()

    if person1 == "f":
        change()
    else:
        if person1 == "g":

            print ("GOOO!!")

def race_2():
    print ("You chose the race of the Person....")
    time.sleep(0.5)

    race_2 = {
        "life :" : 2000,
        "Damage :" : 300,
        "Critical Damage" : 450
    }

    for x,y in race_2.items():

        print (x,y)
      
        
    print ("If you wish to change race, press the f key.")
    print ("If you wish to continue press g")

    person1 = input ()

    if person1 == "f":
        change()
    else:
        if person1 == "g":

            print ("GOOOO!!")


def race_1():
    print ("You chose the race of the Alien....")
    time.sleep(1)

    race_1 = {
        "life :" : 3500,
        "Damage :" : 235,
        "Critical Damage :" : 300
    }

    for x,y in race_1.items():

        print (x,y)
      
        
    print ("If you wish to change race, press the f key.")
    print ("If you wish to continue press g")

    person1 = input ()

    if person1 == "f":
        change()
    else:
        if person1 == "g":

            print ("GOOO!!")

def creation():
    
    name = input ("Nombre del personaje : ")
    time.sleep(2)
   
def change():

    race = {
        "Race 1 :" : "Monster",
        "Race 2 :" : "Person",
        "Race 3 :" : "Alien"
    }

    print ("Choose a race:  ")
    time.sleep(2)
    for x,y in race.items():
        
        print (x,y)
    
    person1 = input ()

    if person1 == "Race 1":

        race_1()
    else:
        if person1 == "Race 2":

            race_2()
        else:
            if person1 == "Race 3":

                race_3()
    
creation()
change()
