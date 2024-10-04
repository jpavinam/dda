pares = 0 #iniciar el contador en cero

num = int(input("Escribe un número: "))

while num != 0:
    if num % 2 == 0:
        pares = pares +1 #contar si es par
    num = int(input("Escribe un número: "))

print(f"Escribiste {pares} números pares")