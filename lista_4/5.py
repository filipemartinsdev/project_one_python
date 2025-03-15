# Escreva um programa que receba uma lista de números e retorne uma nova lista contendo apenas os números pares.

def evenList(input):
    output = []
    for i in input:
        if(type(i) != int and type(i) != float):
            continue
        if (i % 2 == 0):
            output.append(i)
    return output 

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, None, True, False]
print(evenList(myList))       