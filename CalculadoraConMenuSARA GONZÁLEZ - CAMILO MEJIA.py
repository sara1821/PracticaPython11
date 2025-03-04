def sumar(a,b):
    return a + b 

def resta(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b 
def dividir(a,b)
    if b == 0:
        return "Error: Division por cero"
    
def mostrar_menu()
    print("Calculadora Básica SaraGonzalezyCamiloMejia")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break    
        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("introduce el primer numero: "))
            num2 = float(input("introduce el segundo numero: "))
        if opcion == '1':
            resultado = sumar(num1, num2)
            print(f"El resultado de {num1} + {num2} es: {resultado}")
        elif opcion == '2':
            resultado = restar(num1, num2)
            print(f"El resultado de {num1} - {num2} es: {resultado}")
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
            print(f"El resultado de {num1} * {num2} es: {resultado}")
        elif opcion =='4':
            resultado = dividir(num1, num2)
            print(f"El resultado de {num1} / {num2} es: {resultado}")
    else:
        print("Opción no válido. Por favor, selecciona una opción del 1 al 5")
    if__name__"__main__":
    calculadora()