# Algoritmo
# - calcular a soma de 1 a 100 com laço FOR

def printSumSequence(n):
    output = 0
    for i in range(n + 1):
        output += i
    print(output)
    
printSumSequence(100)