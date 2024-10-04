c1 = float(input("Calificación 1: "))
c2 = float(input("Calificación 2: "))
c3 = float(input("Calificación 3: "))

prom = (c1 +c2 +c3) / 3.0

if prom >= 60:
    print("Aprobaste el curso")
else:
    print("Reprobaste el curso")