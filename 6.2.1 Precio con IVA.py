precio  = float(input("Escribe el precio: "))

while precio < 0:
    print("El precio no puede ser negativo")
    precio = float(input("Escribe el precio: "))

print(f"El precio con IVA es {precio*1.16:,.2f}")