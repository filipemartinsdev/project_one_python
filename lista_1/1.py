# Escreva um programa que receba um número e verifique se ele é positivo, negativo ou zero.

def checkNumber(n):
    if(type(n) != int and type(n) != int):
        return TypeError
    if(n < 0):
        return "n < 0"
    elif(n == 0):
        return "n == 0"
    elif(n > 0):
        return "n > 0"
print(checkNumber(10))
print(checkNumber(-10))
print(checkNumber(None))
print(checkNumber("10"))




