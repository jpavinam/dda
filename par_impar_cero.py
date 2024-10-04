num = int(input("Escribe un numero: "))

if num == 0:
    print("Es cero")

if num != 0 and num % 2 == 0:
    print("Par")

if num % 2 != 0:
    print("Impar")

if num == 0:
    print("Es cero")
elif num % 2 == 0:
    print("Par")
else:
    print("Impar")