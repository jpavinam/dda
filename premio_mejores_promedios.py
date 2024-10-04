p1 =float(input("Escribe Promedio 1: "))
p2 =float(input("Escribe Promedio 2: "))
p3 =float(input("Escribe Promedio 3: "))

if p1 > p2 and p1 > p3:
    # Aquí, el 1 es el ganador
    print("El promedio 1 gana 15 GB")
    if p2 > p3:
        print("El promedio 2 gana 10 GB")
        print("El promedio 3 gana 5 GB")
    else:
        print("El promedio 3 gana 10 GB")
        print("El promedio 2 gana 5 GB")
elif p2 > p3 and p2 > p1:
    # En esta parte, el 1 no es el primer lugar
    print("El promedio 2 gana 15 GB")
    if p1 > p3:
        print("El promedio 1 gana 10 GB")
        print("El promedio 3 gana 5 GB")
    else:
        print("El promedio 3 gana 10 GB")
        print("El promedio 1 gana 5 GB")
else:
    print("El promedio 3 gana 15 GB")
    if p2 > p1:
        print("El promedio 2 gana 10 GB")
        print("El promedio 1 gana 5 GB")
    else:
        print("El promedio 1 gana 10 GB")
        print("El promedio 2 gana 5 GB")

