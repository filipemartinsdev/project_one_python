# Escreva um programa que calcule e imprima a soma dos números de 1 a 100 usando um laço `for`.

def printSumSequence(n):
    output = 0
    for i in range(n + 1):
        output += i
    print(output)
    
printSumSequence(100)


