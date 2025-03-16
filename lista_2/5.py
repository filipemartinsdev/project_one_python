# Escreva um programa que receba uma string e conte quantas vogais ela contém.

def vowalCount(word):
    count = 0
    for char in word:
        if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
            count += 1
    return count
print(vowalCount("python"))
print(vowalCount("HTML"))
print(vowalCount("Java Script"))