# Escreva um programa que receba uma string e conte quantas palavras ela contém.

def strToList(input):
    if(type(input) != str):
        return TypeError
    array = []
    for i in input:
        array.append(i)
    return array

def countWords(input):
    newStr = strToList(input)
    count = 1
    
    last = None
    for i in newStr:
        # print(last)
        # print(count)
        if(last == ' ' and i != ' '): 
            count += 1
        last = i
    return count

print(countWords("python, HTML"))
print(countWords("python git"))
print(countWords("git"))