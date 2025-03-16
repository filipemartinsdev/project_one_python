# Escreva um programa que receba um número \( N \) e imprima os primeiros \( N \) números pares.

def printEven(n):
    i = 0
    while(i <= n):
        if(i % 2 == 0):
            print(i)
        i+=1
    return

printEven(10)

