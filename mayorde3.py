A = int(input("Escribe el numero 1: "))
B = int(input("Escribe el numero 2: "))
C = int(input("Escribe el numero 3: "))

if A > B and A > C:
    print("El mayor es ", A)
else:
    if B > C:
        print ("El mayor es  ", B)
    else:
        print("El mayor es  ", C)
