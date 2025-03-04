horas_vuelo = []
for i in range(1, 11):
    horas = float(input(f"¿Cuántas horas vuela la nave en el día {i}? "))
    horas_vuelo.append(horas)
promedio = sum(horas_vuelo) / len(horas_vuelo)
print(f"\nEn los últimos 10 días, el promedio en horas de vuelo diario es: {promedio:.2f} horas")
