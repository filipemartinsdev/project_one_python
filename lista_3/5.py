# Escreva uma função que receba uma string e retorne o número de vogais nela. A função deve ser modular para ser usada em diferentes contextos onde seja necessário contar vogais em textos.

def vowelCount(word):
    count = 0
    for i in word:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            count += 1 
    return count