A = int(input("Ingrese el límite inferior (A): "))
B = int(input("Ingrese el límite superior (B): "))

while A > B:
    print("El límite inferior debe ser menor que el límite superior.")
    A = int(input("Ingrese el límite inferior (A): "))
    B = int(input("Ingrese el límite superior (B): "))

suma = 0
cont = A
while cont <= B:
    suma = suma + cont
    cont = cont + 1

print(f"La suma de los números comprendidos entre {A} y {B} es {suma}")