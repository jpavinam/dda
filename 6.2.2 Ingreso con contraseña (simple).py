intentos = 0
contra = input("Ingrese contraseña: ")
intentos = intentos + 1

while not contra == "hola123" and not contra == "#" and intentos < 5:
    print("La contraseña no es correcta.")
    contra = input("Ingrese contraseña: ")
    intentos = intentos + 1

if contra == "hola234":
    print("Cotraseña correcta. Felicidades.")
else:
    print("Gracias por participar")