# Escreva um programa que receba uma string e retorne a string invertida

def invertStr(input):
    if(type(input) != str):
        raise TypeError("Parâmetro deve ser tipo String")
    charList = []
    
    for char in input:
        charList += char
    i = len(input) - 1
    output = ""
    while(i >= 0):
        output += charList[i]
        i = i - 1
    return output

print(invertStr("palindromo"))
print(invertStr(None))