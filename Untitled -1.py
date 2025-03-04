numero = int(input("Ingrese un numero de tres digitos: "))

if 100 <= numero <= 999:
    numero_invertido = int(str(numero)[::-1])
    print(f"El numero invertido es: {numero_invertido}")
else:
    print("Por favor, ingrese un numero de tres digitos valido.")