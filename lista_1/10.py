# Escreva um programa que receba o preço de um produto e classifique-o como barato (menor que 50), normal (entre 50 e 100) ou caro (acima de 100).

def checkPrice(n):
    if(type(n) != int and type(n) != float):
        return "type error"
    if(n < 50):
        return "barato"
    elif(n >= 50 and n < 100):
        return "normal"
    else: return "caro"

print(checkPrice(-10))
print(checkPrice(100))
print(checkPrice(10_000))

