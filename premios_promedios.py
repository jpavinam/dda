p1 = float(input("Escriba promedio 1: "))
p2 = float(input("Escriba promedio 2: "))
p3 = float(input("Escriba promedio 3: "))

if p1 > p2 and p1 > p3:
    #el promedio 1 es el mayor
    l1 = 1
    if p2 > p3:
        l2 = 2
        l3 = 3
    else:
        l2 = 3
        l3 = 2
elif p2 > p3:
    # el promedio 2 es el mayor
    l1 = 2
    if p1 > p3:
        l2 = 1
        l3 = 3
    else:
        l2 = 3
        l3 = 1
else:
    # el promedio 3 es el mayor
    l1 = 3
    if p2 > p1:
        l2 = 2
        l3 = 1
    else:
        l2 = 1
        l3 = 2

print(f"El promedio {l1} gana 15 GB")
print(f"El promedio {l2} gana 10 GB")
print(f"El promedio {l3} gana 5 GB")



