

while True:
    name = input("Enter your name :")
    length = len(name)
    if length <= 3 :
        print ("name too short")
    elif length >= 10:
        print ("name too long")
    else:
        print ("correct name")
        
        break
while True:
    print ("Enter a password:",end="")
    password =input()
    length = len(password)

    if length <= 3 :
        print ("Password is too short")
    elif length >= 10:
        print ("The password is too long")
    else:
        print ("Correctly completed")

        break



import getpass

print ("Enter your name:",end="")
user = input()
attempts = 0
while True:
    if user != name:
        attempts += 1
        print ("incorrect user name")
        print (" Enter your name :",end="")
        user = input()
    if attempts == 2:
        print ("End of program")
        break
        
    
    if user == name:
        attempts= 0
        password = getpass.getpass("password:" )
        while True:
            
            if password != password:
                attempts += 1
                print ("password incorrect")
                
            if attempts == 2:
                print ("End of program")
                break    
            
            if password == password:
                print ("Account successfully created")
        
                break
       
    





