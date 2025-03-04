import math

radio = float(input("Ingresa el radio del circulo"))
perimetro = 2 * math.pi * radio
area = math.pi * (radio ** 2)

print(f"El perimetro del circulon es: {perimetro:.2f}")
print(f"El area del circulo es: {area:.2f}")
