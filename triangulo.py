l1 = float(input("Longitud del lado 1: "))
l2 = float(input("Longitud del lado 2: "))
l3 = float(input("Longitud del lado 3: "))

if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    print("No válido")
elif l1 == l2 and l1 == l3:
    print("Equilátero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Isósceles")
else:
    print("Escaleno")