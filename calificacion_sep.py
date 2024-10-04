calif  = input("Escribe la calificación: ")
calif = float(calif)

if calif < 0 and calif > 10:
    print("No válido")
elif calif < 6.0:
    print("CINCO")
elif calif < 6.5:
    print("SEIS")
elif calif < 7.5:
    print("SIETE")
elif calif < 8.5:
    print("OCHO")
elif calif < 9.5:
    print("NUEVE")
else:
    print("DIEZ")