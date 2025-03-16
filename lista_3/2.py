# Escreva uma função que receba um número e retorne `True` se ele for par e `False` caso contrário. A função deve ser modular para ser usada em diferentes contextos onde seja necessário verificar a paridade de um número.

def isEven(n):
    if(type(n) != int and type(n) != float): return None
    if(n % 2 == 0): return(True)
    else: return False
print(isEven(2))
print(isEven(4))
print(isEven(67))