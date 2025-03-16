# Escreva um programa que receba um número e calcule seu fatorial usando um laço `for`.

def calcFactorial(n):
    output = 1
    count = 0
    while(count < n):
        output = output * (n - count)
        count += 1
    return output
print(calcFactorial(1))
print(calcFactorial(2))
print(calcFactorial(3))
print(calcFactorial(4))
print(calcFactorial(5))

