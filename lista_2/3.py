# Escreva um programa que receba um número e imprima sua tabuada de 1 a 10.

def printTab(n):
    for i in range(11):
        print(n, "x", i, "=", n*i)

printTab(5)
