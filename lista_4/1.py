# Escreva um programa que receba uma lista de números e calcule a soma de todos os seus elementos

def sumList(list):
    output = 0
    for i in list:
        output += i    
    return output

print(sumList([1, 2, 3]))
print(sumList([-2, 1, 1]))
print(sumList([-100, -100 ]))