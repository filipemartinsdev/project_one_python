# Escreva um programa que receba um número e verifique se ele é divisível por 3 e 5 ao mesmo tempo.

def checkDivision(n):
    if(n % 2 == 0 and n % 5 == 0):
        return True
    else: return False
    
print(checkDivision(25))
print(checkDivision(9))
print(checkDivision(90))

