# Escreva uma função que receba o raio de um círculo e retorne sua área. A função deve ser reutilizável para calcular a área de qualquer círculo sem precisar reescrever a lógica de cálculo.

# FORMULA DA AREA: PI * R^2

def calcArea(R):
    output = 3.14 * (R * R)
    return output
print(calcArea(3))
print(calcArea(6))
print(calcArea(12))

