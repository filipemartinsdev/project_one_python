# Escreva uma função que receba um número e retorne seu fatorial. A função deve ser reutilizável para calcular o fatorial de qualquer número sem precisar reescrever a lógica de cálculo.

def factorial(n):
    count = 1
    output = 1
    
    while(count <= n):
        output = output * count        
        count += 1
    return output