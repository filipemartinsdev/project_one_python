# Escreva uma função que receba uma lista de números e retorne a média deles. A função deve ser modular para ser usada em diferentes contextos onde seja necessário calcular a média de uma lista de valores.

def calcMedia(*args):
    output = 0
    j = 0
    for i in args:
        output += i
        j+=1
    output /= j
    return output