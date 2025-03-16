# Escreva um programa que receba um ano e verifique se ele é bissexto.
def isLeapYear(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    return False
    
print(isLeapYear(1999))
print(isLeapYear(2025))
print(isLeapYear(2020))
print(isLeapYear(2012))
