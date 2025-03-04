notas = []

for i in range(1, 5):
    nota = float(input(f"Ingrese la nota {i}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio:.2f}")
