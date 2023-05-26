import time
def cuenta_atras(limite):
    num = 6
    
    while num > limite:

        yield num - 1
        num = num - 1

cuenta = cuenta_atras(0)

print (next(cuenta))
time.sleep(1)
print (next(cuenta))
time.sleep(1)
print (next(cuenta))
time.sleep(1)
print (next(cuenta))
time.sleep(1)
print (next(cuenta))
time.sleep(1)
print (next(cuenta))





