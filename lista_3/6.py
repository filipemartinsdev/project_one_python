# Escreva uma função que receba uma string e retorne `True` se ela for um palíndromo (lê-se igual de trás para frente) e `False` caso contrário. A função deve ser modular para ser usada em diferentes contextos onde seja necessário verificar palíndromos.

# reutilizando a função do exercicio 4 da lista 4:

def invertStr(input):
    charList = []
    for char in input:
        charList += char
    i = len(input) - 1
    output = ""
    while(i >= 0):
        output += charList[i]
        i = i - 1
    return output

def isPalindrom(input):
    if(type(input) != str):
        return TypeError
    if(input.upper() == invertStr(input).upper()):
        return True
    else: return False
    
# print(isPalindrom("Ana"))
# print(isPalindrom("garrafa"))
# print(isPalindrom("101"))
# print(isPalindrom(None))
# print(isPalindrom("nOn"))

# print(isPalindrom(""))

print(
    isPalindrom("Ana")
)
