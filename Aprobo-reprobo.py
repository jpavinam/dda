calif = float(input("Escribe tu calificación: "))

if calif >= 0 and calif <= 100:
    if calif >= 70:
        print("Aprobaste el curso")
    else:
        print("Reprobaste el curso")
else:
    print("Calificación no válida. Se asignará 50. Reprobaste")
