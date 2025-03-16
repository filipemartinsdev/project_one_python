# Escreva uma função que receba um número \( N \) e retorne uma lista com a sequência de Fibonacci até \( N \). A função deve ser modular para ser usada em diferentes contextos onde seja necessário gerar a sequência de Fibonacci.

def seqFibonacci(n):
    output = [1, 1]
    i = 1
    while(output[len(output) - 1] < n):
        output.append(output[i] + output[i-1])
        i+=1
    return output
print(seqFibonacci(5))
print(seqFibonacci(10))
print(seqFibonacci(50))