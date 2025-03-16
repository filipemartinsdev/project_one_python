# Escreva um programa que receba um número e verifique se ele é primo usando um laço `for`.

def checkDivisors(n):
    output = []
    i = 1
    while(i < 10):
        if(n % i == 0):
            output.append(i) 
        i += 1
    return output

def checkPrimo(n):
    if(len(checkDivisors(n)) > 2):
        return False
    else: return True
    
print(checkPrimo(0))
print(checkPrimo(3))
print(checkPrimo(10))
print(checkPrimo(253))
    